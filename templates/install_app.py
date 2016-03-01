import re

execfile("{{ovp_tmpdir}}/was_import/wasadminlib.py")

ovp_clusters = {{ovp_clusters}}

app_cl = {}
for cluster in ovp_clusters:
    for app in cluster["apps"]:
        if app in app_cl:
            app_cl[app].append(cluster["name"])
        else:
            app_cl[app] = [cluster["name"]]

installed_apps = listApplications():
#installed_apps = [ "Ovp-Admin-15.3.0.war", "SchedulerTask-15.3.0-AD.jar" ]

for app in app_cl.keys():
    for app_name in installed_apps:
        if re.split("war|jar", app)[0] == re.split("war|jar", app_name)[0]:
            print app, "already installed"
            break
        elif re.split("\d+\.\d+\.\d+\.", app)[0] == re.split("\d+\.\d+\.\d+\.", app_name)[0]:
            print "update", app_name
            updateApplication("{{ovp_tmpdir}}/%s" % app)
            AdminConfig.save()
            break
        elif app not in [re.split("\d+\.\d+\.\d+\.", a)[0] for a in installed_apps]:
            print "install", app, app_cl[app]
            installApplication("{{ovp_tmpdir}}/%s" % app, [], [app_cl[app]], [])
            AdminConfig.save()
            break
