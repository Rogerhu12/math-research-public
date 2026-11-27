# Run10：完整真实输入重建与进行中标量记录

2026-11-27，Astra-larger-e4e2a2bf-20261126。

本次新公开runner用于继续完整课题。09原ff544科学仍在运行；未从已运行时长推断hang、科学失败或结束。新的完整closure值复用源码正在针对实际调用结构制作，保留所有方程、变量、32阶段、原范数/判据与预算，不把已登记的解析frame/J3重报为新优化。本次先准备后继必需的完整原warm/reference输入，真正输入身份必须待此runner实际返回后冻结。

## 完整启动程序

三个完整运行文件分别为：

- `scripts/resume_20261126/public_actions_controller_parallel10_compact_metadata.py`：19587B / `071eb470042a1de469bdef4b7bb651791a19bb2f47565bb5245633dd08cbecf9`；
- `scripts/resume_20261126/public_actions_followups_with_active_progress.py`：32762B / `046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314`；
- 根workflow `.github/workflows/visible-larger-20261127-parallel10.yml`：2228B / `4e0afa7e5c336eef0a4bb4e0ba0539c316b6b54c30d63d85681e7daa73e9dc95`。

旧09控制器e386与旧followups3cb1完整文件继续保留。新控制器有独立10 HANDOFF标记、工作区、concurrency group和请求路径；既有09请求/源码/子进程不改。科学进程仍在每步固定的detached sparse worktree运行；出版pull不能替换它已加载的模块。GitHub凭据仍只在编排父进程环境中，科学子进程的原三类token环境删除代码完整保留。

workflow保原350分钟、controller保20000秒；到编排预算只关闭新准入，已启子进程仍按原程序观察自然返回，workflow实际终态另记，不将时限叫完成。Python3.12.14、NumPy2.3.5、SciPy1.17.0、CPUtorch2.5.1与原BLAS单线程环境完整保。原checkout/setup-python固定action提交、blob:none和sparse checkout也完整保。每次实际pull核两README差异，至少3000秒核一次；root云API核查不冒pull。

## 全参数输入重建

新request保持完整561308原warm recipe、五个原prefix和四个原warm步骤，科学source和所有默认/显式参数仍由完整已刊源约束。队列唯一初始步骤是完整4e655 reference producer：原24 argv、全部5输出、42个标量选择器与原09实际2对象逐值相同，仅新step id、用途和来源说明改变。完整对象见[10队列](../computations/resume-20261127-followups-10.json)，原对象和真实09返回完整保[原2–5卷一归档](../computations/run09-returned2-5-complete-archive-part-001.json)。

M160/J923/N2048/P7377、1845原legacy及5532原Gauss观测、八阶原seed积分、128 panels、300秒原scalar admission、1e−18原积分容差、1/8原尾切和全部十一原history不删。没有复制09既知ref-report哈希到未返回10，也没有把可能改变的参考尾叶数预填为1995。固定g/全部chart words、scalar parameters和原地址关系要从真正新返回核明；必要重建不是新的旧结论证明。原07/08未返typed、保护/发现顺序和09适用真实父义务全部保留。

## 进行中的只读进度

原followups的完整 `run_step` 函数文本逐字未改；新可选 `progress_summary` 只提供正在运行子进程的显式有界scalar观察。它每300秒最多读取4件各严格小于95000B的小JSON，每件先stat，再两次有界完整捕获并比字节。最多48个显式标量字段，字符串最多512B，整份公开compact观察严格小于8000B；全源保留所有这些界与缺失/改变/超界处理。文件不存在或正在更新会留下观察错误，不更改科学退出/步骤结果/原输入或再运行任何科学算子。

只有这类明确请求的小progress文件会被观察；原大report、根包、坐标/逐胞数组不作为进度文件。完整小文件SHA、字节数、两捕获一致性、原科学源commit/SHA、step id、PID和观察时间均绑定。报告明确写child仍未自然返回；不会增加completed计数，也不会凭scalar进度生成完整field、metric或geometry证书。所有原始progress文件和完整观察历史留runner，公开保存短标量记录；后来真实返回仍由原完整输出/摘要逻辑处理。

当前初始warm/reference步骤没有配置进度选择器，执行字段与原对象完全一致。未来全源可以原子写一个小progress.json，分别记录residual、statistics、fullscan与实际cache计数，再在完整后继计划内显式给选择器。不能凭没有更新的进度推断数值失败或少做原函数复核。

## 来源核查与当前状态

本次只做完整源文字/身份/完整参数比较，未声称失联后AST/compile或本地科学运行。新controller的完整scientific main除导入完整新followups文件名外逐字等于原体；新followups的原完整run_step逐字等于3cb1。记录支持和其格式守卫不会删除数学条件，也不是新的数学准入前门。

规则云核commit `8fa535aed5ae04e39b05a705868f761df7935d83`；两README整SHA仍581402/3c1c无变。完整前交接保ccb52315固定H之后压缩当前历史文字，为10独立真实slot留容量。实际run编号、启动、六输入和后继新场的值/身份待真实返回登记；本说明不预先宣称任何一步已跑、成功、同g或题目完成。
