import re

execfile("{{ovp_tmpdir}}/was_import/wasadminlib.py")

ovp_clusters = {{ovp_clusters}}
ovp_app_dist_names = {{ovp_app_dist_names}}

app_cl = {}
for cluster in ovp_clusters:
    for app in cluster["apps"]:
        if app in app_cl.keys():
            app_cl[app].append(cluster["name"])
        else:
            app_cl[app] = [cluster["name"]]

installed_apps = listApplications()

for app in app_cl.keys():
    appname = re.split("\.war|\.jar", app)[0]
    if appname in [re.split("\.war|\.jar", a)[0] for a in installed_apps]:
        print app, "already installed"
    elif re.split("\d+\.\d+\.\d+\.", app)[0] in [re.split("\d+\.\d+\.\d+\.", a)[0] for a in installed_apps]:
        print "update", app_name
        updateApplication("{{ovp_tmpdir}}/%s" % app)
        AdminConfig.save()
    elif app not in [re.split("\d+\.\d+\.\d+\.", a)[0] for a in installed_apps]:
        print "install", app, app_cl[app]
        installApplication("{{ovp_tmpdir}}/%s" % app, [], app_cl[app], ["-appname", appname])
        AdminConfig.save()
        print "check that application %s is ready" % app
        for time in range(1,2):
            if isApplicationReady(appname):
                break
            else:
                sleep(5)

# start servers
for cluster in ovp_clusters:
    print "Start all servers in cluster %s" % cluster["name"]
    startAllServersInCluster(cluster["name"])

#startAllApplications()
