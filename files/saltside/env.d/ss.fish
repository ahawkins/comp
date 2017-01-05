function ss --description "Everything for Saltside"
	switch $argv[1]
		case 'notes'
			set -l year (date '+%Y')
			set -l week (date '+%V') # 00-53
			set -l week_number (math "$week+1")
			set -l notes_file "{{ notes_dir }}/$year-w$week_number.md"

			eval $EDITOR $notes_file
		case 't'
			if test (count $argv) -ge 2
				command todo.sh -d ~/.config/saltside/todo.sh $argv[2..1]
			else
				command todo.sh -d ~/.config/saltside/todo.sh ls
			end
		case '*'
			saltside-workstation $argv
	end
end
