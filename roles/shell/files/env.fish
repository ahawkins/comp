# Set directory for s code management tool. See ahawkins/bindir
set -x S_SRC_DIR {{ s_src_dir }}

# # Go GOPATH for all go toolchain things
# set -x GOPATH {{ gopath }}
# set -x PATH {{ gopath }}/bin $PATH

# Add bindir to path
set -x PATH {{ bindir_dir }}/bin $PATH

set -x LIFE_DIR {{ life_dir }}

# Set jrnl entry directory
set -x JOURNAL_DIR {{ life_dir }}/journal

# # Set a personal token token to avoid GitHub's rate limit.
# # This must come after adding bindir to PATH because bindir provides
# # comp-secret
# set -x HOMEBREW_GITHUB_API_TOKEN (comp-secret {{ keys.brew_api_token }})

# Source comp specific configurations
for env_file in (find ~/.config/comp/env.d -type f -print)
	source $env_file
end
