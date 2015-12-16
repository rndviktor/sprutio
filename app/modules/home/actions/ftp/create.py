from core import FM


class CreateFtp(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(CreateFtp, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        request = self.get_rpc_request()

        result = request.request('ftp/create_connection', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), host=self.params.get('host'),
                                 ftp_user=self.params.get('user'),
                                 ftp_password=self.params.get('password'))

        answer = self.process_result(result)
        return answer
