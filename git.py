import web
import commands
urls=(
    '/pull','git',
)

class git:
    def GET(self):
        (status,output) = commands.getstatusoutput('bash pull.sh')
        return "success"

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()