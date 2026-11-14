# 根 README 新规与真实 rebase 发布

2026-11-12 16:37 UTC，实际 `git pull main` 返回0，root随后立即读两README差异。已读提交为 `1cede392a5e0b8ba79bd444b12dc6f3edb7b4423`。根 README 改了日志与推送规则，topic README 未变。按照用户“有变立即遵行”，现在停止写根 `LOG.md` 及其归档；跨课题说明只追加本题 log。推送非快进拒绝后立即 `git pull --rebase`，再检查README并继续普通推送。

旧第12批本地发布11434/0d6af4真实exit78：它先完成pull0、打印新规则差异，然后在创建payload前返回。没有检查点提交或main推送，更没有新根日志写入。原差异和真实收据一并保留。

## 实际实现

新的 `fd2d_publish_rebase_checkpoint.py` 只运行于可丢弃CI克隆的 `fd2d-ci-publisher` 分支。第一次仍以准确Git树身份覆盖明确的本题文件，完整保留所有非本题条目。根LOG既不读取、修改，也不归档。首次普通push若遭竞争，立即执行真实 `git pull --rebase --no-stat origin main`，随后检查根及topic README差异。原payload源/数据若因重放发生任何身份变化，返回79供owner读取真实冲突，不把未经重求的合并内容冒成原闭存文件。

每次成功pull的SHA和时间写进H；只修改尚未推送的本会话提交来更新这条记录。不force，不改写别人的已推历史。实际main push循环至成功；若规则变化返回78供owner立即读取遵行，数学工作持续。CI bootstrap及batch builder已改用此路径，request v2不再含root-log写入请求。原旧发布器仅作为已完成历史的源码保留，不由新workflow消费者调用。

本地payload检查点工具仍只创建本会话新的独立payload分支，不动main；其成功pull后两README检查和H更新时间保持，兼容“下次pull不晚于”的明确记录。

## 一次具体竞争验证与真实失败

测试只创建临时本地Git仓库。pre-push时另一个clone用普通push提交外部文件变化，真实触发当前push的旧值竞争；未连接任何外部远端，也未使用令牌。

首次fixture16200/9a357a真实exit1，原测试在断言前未保存底层stdout，只确认没有观察到预期两次pull；checker源码保留。第二次19180/aa534c真实exit1，完整stdout明确服务器用 `incorrect old value provided` 报真实CAS竞争。新发布器最初仅识别GitHub此前见过的 `fetch first`/`non-fast-forward`/`cannot lock ref...but expected` 文字，因此没有进入重放；该失败源和真实报告保留。随后只新增这一确切CAS格式的识别，不把权限或网络错误猜作并发冲突。

第三次62791/207d15真实exit0，8.18469秒：普通竞争case实际两次pull、push退出[1,0]，第二次为真实rebase，最后远端同时含本payload与外部新提交。根LOG的Git blob身份完全不变。另一case在外部提交同时修改README时，真实rebase后立刻打印差异并exit78，远端仍只含外部提交，本payload未推。它是预期的规则保护结果；测试整体exit0。

这解决的是仓库新规和普通Git发布，不改数学字段、任何BVP目标或完成标准。
