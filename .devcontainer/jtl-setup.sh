
# Clean out distracting files we no longer need. 
TARGET_DIR=$1

#cd "$TARGET_DIR" || exit 1

rm -rf .devcontainer .github .lib requirements.txt LICENSE  
mv lessons/* .
rm -rf lessons 
git add -A 
git commit -m "codeserver init"
