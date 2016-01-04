import web
import commands
urls=(
    '/pull','git',
)

class git:
    def GET(self):
        (status,output) = commands.getstatusoutput('bash pull.sh')
        return 'output:'+output

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()