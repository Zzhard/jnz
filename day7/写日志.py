

# error
# waring
# info
# debug
import nnlog
log = nnlog.Logger('my.log',level='info',backCount=5,when='D')
log.info('xiaojun登陆...')
log.error('数据连接失败！')
log.surprise()

