vm_list = ['test1']

Vagrant.configure(2) do |config|

  for vm_name in vm_list do
      config.vm.define vm_name do |vmn|
          vmn.vm.box = "boxcutter/ol67"

          provider = (ARGV[2] || ENV['VAGRANT_DEFAULT_PROVIDER'] || :virtualbox).to_sym

          if provider == :virtualbox
              vmn.vm.provider "virtualbox" do |vb|
                vb.gui = false
                vb.memory = "1024"
              end
          end

          if provider == :parallels
              vmn.vm.provider "parallels" do |prl|
                prl.memory = "1024"
                prl.name = "test1"
                prl.linked_clone = true
                prl.update_guest_tools = false
                prl.check_guest_tools = false
              end
          end

          vmn.vm.hostname = vm_name
          vmn.vm.network :forwarded_port, guest: 8088, host: 8088 # storm ui

        #  config.vm.provision "shell", inline: <<-SHELL
        #     sudo yum update -y
        #  SHELL

          vmn.vm.provision "ansible" do |ansible|
            ansible.verbose = "v"
            ansible.groups = {
              "zookeeper" => ["test1", "test2"],
              "storm" => ["test1", "test2"],
              "all_groups:children" => ["zookeeper", "storm"]
            }
            ansible.playbook = "playbook.yml"
          end
      end
  end
end
