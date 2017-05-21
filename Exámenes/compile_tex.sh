for tex_path in $( ls -d 201*/ ); do
 cd $tex_path
 for tex_file in $( ls *.tex ); do
  pdflatex $tex_file
 done
 rm *aux *log *gz *out
 cd ..
done
