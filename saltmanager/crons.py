import salt.client

local = salt.client.LocalClient()
result = local.cmd('*', 'cmd.run', ['uptime'])
print result
