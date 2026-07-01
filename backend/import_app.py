try:
    import app.main
    print('app imported successfully')
except Exception as e:
    import traceback
    traceback.print_exc()
