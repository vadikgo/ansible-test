Vagrant.configure(2) do |config|

  config.vm.box = "bento/centos-6.7"

  # Disable the new default behavior introduced in Vagrant 1.7, to
  # ensure that all Vagrant machines will use the same SSH key pair.
  # See https://github.com/mitchellh/vagrant/issues/5005
  config.ssh.insert_key = false

  config.vm.provider "parallels" do |prl|
    prl.memory = "512"
    prl.name = "test1"
    prl.linked_clone = true
    prl.update_guest_tools = false
    #prl.check_guest_tools = false
  end

  config.vm.hostname = "test1"

#  config.vm.provision "shell", inline: <<-SHELL
#     sudo yum update -y
#  SHELL

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end
end
