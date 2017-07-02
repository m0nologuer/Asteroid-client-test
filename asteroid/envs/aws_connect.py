import boto.ec2, time, paramiko, os

class AWSConnect(object):
	"""Base class for a 3D scene"""
	def connect():
		ec2 = boto.ec2.regions()[3].connect()
		image_id = 'ami-ad7e2ee8'
		image_name = 'Ubuntu 10.10 (Maverick Meerkat) 32-bit EBS'
		new_reservation = ec2.run_instances(
		    image_id=image_id,
		    key_name='calif_keys',
		    security_groups=['web'])

		instance = new_reservation.instances[0]

		print "Spinning up instance for '%s' - %s. Waiting for it to boot up." % (image_id, image_name)
		while instance.state != 'running':
		    print "."
		    time.sleep(1)
		    instance.update()

		print "Instance is running, ip: %s" % instance.ip_address

		print "Connecting to %s as user %s" % (instance.ip_address, 'ubuntu')

	def upload_user_files():
		transport = paramiko.Transport((myhost, 22))
		transport.connect(username = myusername, password = mypassword)

	def start_process()
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(instance.ip_address, username='ubuntu', key_filename=os.path.expanduser('~/.ssh/test'))
		ssh.exec_command
		stdin, stdout, stderr = ssh.exec_command('echo "TEST"')
		print stdout.readlines()
		ssh.close()

