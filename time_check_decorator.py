import arrow


def ts_check_decorator(func):
    def in_time(*args, **kwargs):
        begin = min(*args, **kwargs)
        end = max(*args, **kwargs)
        ts = arrow.get().timestamp
        if end > ts > begin:
            print('in time')
        else:
            print('Not in time')
        return func(*args, **kwargs)

    return in_time


@ts_check_decorator
def add(begin_at, end_at):
    print('begin_at:{}, end_at:{}'.format(begin_at, end_at))


if __name__ == '__main__':
    print('-' * 10)
    begin_at = arrow.get().replace(days=-1).timestamp
    end_at = arrow.get().replace(days=1, hours=-1).timestamp
    add(begin_at, end_at)

    begin_at = arrow.get().replace(days=1).timestamp
    end_at = arrow.get().replace(days=1, hours=1).timestamp
    print('-' * 10)
    add(begin_at, end_at)
