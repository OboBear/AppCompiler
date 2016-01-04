import web
import commands
import os

urls=(
    '/pull','git',
)

class git:
    def GET(self):
        # (status,output) = commands.getstatusoutput('bash pull.sh')
        # return "success"
        os.system('pull.sh')
        return 'success'

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()