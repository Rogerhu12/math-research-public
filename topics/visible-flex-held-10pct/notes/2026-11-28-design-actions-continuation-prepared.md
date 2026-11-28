# 独立 Actions 原 δ-design 连续执行入口

日期：2026-11-28。状态：入口已准备并完成有限静态/实际小投影核验，尚未 dispatch。此记录不含新 BVP 返回或新的数学结论。

## 为什么换执行环境

本地最新真实 λ=.128/M48 全 nodal 状态仍保留，原哈希 `e889dd15…`；没有把反复进程 −9 当作数学失败或已证 OOM。已经核过的 factor-only 映射入口需要约1198.68 MiB磁盘（含512 MiB外余量），本地共享盘余量不足。根 README 第13条明确授权本公开仓库 Actions；第15条仍禁止把可再生的场、矩阵和证书存入仓库或 Release。

GitHub 当前[标准 runner 文档](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)列出公开仓库 ubuntu-latest 为4 CPU、16 GB RAM、14 GB SSD 的独立VM；[系统限制](https://docs.github.com/en/actions/reference/limits)给出单job最多6小时。这些规格不等于新runner实际可用内存或磁盘。新workflow开头实际记录资源，各mesh仍执行既有完整RAM/磁盘门。

## 数值路线

新runner只能使用自己真正生成的输入；没有传送本地数组。原70个静态源共537048字节，通过已绑定的三个公开历史提交逐文件恢复并核SHA。原完整物理port/chart/setup保留。

q=.006起使用已核V3径向分组/CSR表缓存；q=.05/.06使用已经实际成功过的全状态q/warp割线。随后原λ0、λ=.002/M8→M16→M24完整lift和各阶段原门保持。M24材料阶段使用V5解析δ列、direct CSR与完整无环QR；从后续原controller阶段使用已核factor-only映射及逐mesh资源门。

正λ bootstrap直接以M32做 .004/.008/.016，仍由原完整升模与全部门决定。真.032接受后，完整升左右两源再作.064/M40割线，避开已登记的.064/M32谱不足；真.064后同理准备.128/M48，避开旧.128/M40谱不足。若前一真实接受场已经在目标M，则不调用严格要求升M的双源helper，而由原controller执行同M完整割线或仅补左源的完整跨M割线。没有为满足helper接口额外升谱。

原门通过后继续 .192/.256/.384/.512/.75/1，不把恢复阶段作为终点。到.128的旧接受前沿只算必要输入再生。每个真正accepted行都由原 `accepted_original` 重新核后进入累计小记录；未接受的完整nodal也公开其路径/哈希和明确false身份。λ1有限前缀仍未支付真正非线性DN、共同C²闭面时间族及本题其他完成条件。

## 发布、规则检查与任务终止

新workflow仅 `workflow_dispatch`，必须由root提供其实际读过双README的完整commit。CI request中null表示使用这个dispatch值，不是虚构已读提交。root后续可更新request的已读commit。

新worker只用终端git发布自己独占的run/attempt小JSON路径；不用Contents API写回。每个新状态/结论产生即提交推送，非快进拒绝后立即pull--rebase、重查规则再推，禁止force。每次pull都比较根和课题README。若相对已读锚有实际规则差异，只暂停自己拥有的子进程组并发布差异；root读完并更新已读锚后继续同一真实场。无需再次询问用户。凭证仅来自Actions环境/命令行认证，数值子进程环境剥除token/secret/password变量。

每个public结果最多64KiB；原场、全矩阵、因子和证书只留同一runner，不上传仓库、Release或artifact。job350分钟、worker330分钟用于在平台限制前记录实际终态；worker不因一条数值命令返回就销毁同runner输入，可接root下一条已审命令。这些平台执行上限不是课题完成声明。

启动环境请求2线程，但原controller和portable模块仍可能覆盖为1；这里没有实测每阶段BLAS线程数，故不声称全程实际2线程。数值版本保留旧成功workflow的Python3.12、NumPy2.3.5和SciPy1.17.0。

## 已完成的有限检查

三个新Python源的compile/help、原q main精确替换编译、YAML解析、workflow内Python编译和shell bash-n均过。V6的bootstrap与完整lifted-secant两种真实原controller定位标记均逐一恰好匹配。读取已有真实M48工程中断摘要的小投影为13628字节，完整nodal SHA与未接受身份保留；未读场数组、未组J、未跑BVP、未调用git或dispatch。解析代理只读复核了q predictor、两源lift的真实API、port物理绑定与严格升M分支。

全部新来源、六个共享冻结来源、dispatch合同、核验事实和官方链接在相邻JSON中。主代理审阅后登记、推送并实际dispatch；实际run号、runner资源及每次原门返回须另记。
