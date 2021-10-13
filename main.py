from datetime import datetime
import traceback


def main():
    
    # Program timer
    start_time = datetime.now()
    print('> Starting...\n')
    
    try:
        print('Hello, World!')
    
    except KeyboardInterrupt:
        print()
        print('WARNING: Прервано пользователем!')
    
    except Exception as err:
        print()
        print('ERROR: ', err)
        print(traceback.format_exc())
        
    finally:
        
        # LOG: -----------------------------------------------------------------
        print()
        print('Report:', '*' * 40)
        print('    Start time:', start_time.strftime('%d.%m.%Y %H:%M:%S'))
        print('    End time:', datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        print('    Elapsed time:', datetime.now() - start_time)
        print('*' * 48)


if __name__ == '__main__':
    main()
    # print()
    # input('Нажмите "ENTER" для выхода...')
