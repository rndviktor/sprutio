from core import FM


class SaveRules(FM.BaseAction):
    def __init__(self, request, path, params, session, **kwargs):
        super(SaveRules, self).__init__(request=request, **kwargs)

        self.path = path
        self.params = params
        self.session = session

    def run(self):
        request = self.get_rpc_request()

        result = request.request('htaccess/save_rules', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, params=self.params,
                                 session=self.session)
        answer = self.process_result(result)
        return answer
