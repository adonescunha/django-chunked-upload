# -*- coding: utf-8 -*-

from resumable.views import ResumableUploadView
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import simplejson as json
from django.core.files.uploadedfile import UploadedFile
from .files import ChunkedFile

class ChunkedUploadView(ResumableUploadView):

    file_field_name = 'file'
    form = None
    form_template = None

    @property
    def chunks_dir(self):
        return '/tmp'

    def _submit(self):
        files = {}
        r = None

        if self.request.POST.has_key('resumableFilename'):
            r = ChunkedFile(self.storage, self.request.POST)

            if r.is_complete:
                files = {
                    self.file_field_name: self.get_uploaded_file(r.filename, r.file)
                }

        response = self.submit(files=files)

        if r:
            r.delete_chunks()

        return response

    def get(self, *args, **kwargs):
        if self.request.GET.has_key('resumableChunkNumber'):
            return super(ChunkedUploadView, self).get(*args, **kwargs)

        return self.handle_get()

    def post(self, *args, **kwargs):
        action = self.request.POST.get('action')

        if action == 'submit' and not self.request.is_ajax():
            return self._submit()
        elif action == 'validate':
            return self.validate()

        return self.save_chunk()

    def save_chunk(self):
        chunk = self.request.FILES.get(self.file_field_name)
        r = ChunkedFile(self.storage, self.request.POST)

        if r.chunk_exists:
            return HttpResponse('chunk already exists')

        r.process_chunk(chunk)

        return HttpResponse()

    def get_form(self):
        return self.form(data=self.request.POST)

    def get_uploaded_file(self, filename, file):
        return UploadedFile(
            file=file,
            name=filename,
            size=file.size
        )

    def validate(self):
        form = self.get_form()
        del form.fields[self.file_field_name]
        valid = form.is_valid()
        response_dict = {'valid': valid}

        if not valid:
            response_dict['errors'] = form.errors

        return HttpResponse(json.dumps(response_dict),
            mimetype='text/javascript')
