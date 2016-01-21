Vagrant.configure(2) do |config|

  config.vm.box = "bento/centos-6.7"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
  end

  #config.vm.provider "parallels" do |prl|
    #prl.memory = "512"
    #prl.name = "test1"
    #prl.linked_clone = true
    #prl.update_guest_tools = false
    #prl.check_guest_tools = false
  #end

  config.vm.hostname = "test1"

#  config.vm.provision "shell", inline: <<-SHELL
#     sudo yum update -y
#  SHELL

  config.vm.provision "shell", inline: "yum install libselinux-python -y"
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end
end
