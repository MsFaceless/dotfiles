source app_config

if [ ! -f $ENVIROS_PATH ]; then
   mkdir -p $ENVIROS_PATH
fi

echo Creating $ENV_PATH

if [ -f $ENV_PATH ]; then
	rm -r $ENV_PATH
fi
python3 -m venv $ENV_PATH
cd $ENV_PATH
source bin/activate
pip install tg.devtools==2.3.12 transaction==2.3.0 
