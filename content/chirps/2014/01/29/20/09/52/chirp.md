Bash2Scala: for D in $(curl <a href="https://t.co/IBtewkCEcp">https://t.co/IBtewkCEcp</a> | jq '.["england-and-wales"].events[] | .date') ; do echo "new DateTime($D)," ; done