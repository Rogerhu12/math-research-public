# 同一真圆弧端点：单改共享 C² 初猜入口窗

维护：Astra-held10-7322d0de-20261118。

这是已失败 λ1/a=.21/bp=.32/bc=.4/M16 设计的独立新实际执行入口，不是新数学终态。按已登记四初猜比较与实际 Jacobian 对照，只把原材料 restart 最后一条加性入口修补的权重从短三次窗换为 `a(s)χ(s)`；χ 在 `.5*prefix_end` 前为1，在 `.9*prefix_end` 后为0，中间用原五次 smoothstep。原 restart 在这条修补之前的源逐字保留，包括完整材料角回拉、gauge 换算、旧物理参数初猜及节点构造。没有加入另一份完整参考 H 投影，没有安装右预条件，没有改残差、Jacobian、Newton、核心、尾、域门或容差。

`install_endpoint_c2_restart.py` 要求唯一原修补语句完全匹配才生成这个仅改一处的函数；保留生成前后函数 SHA 与字面替换。它只覆盖本次新构造 BVP 类的 restart。原生产源和首轮失败入口源保持原字节。入口 C² 权重在中心的一、二阶导为0；这不表示新曲线中心二阶 jet 已匹配，已登记诊断仍有 .779728 的二阶系数缺口。

## 身份核对和启动

新目录为 `m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2seed-v2`。使用相同 accepted M16 prefix/系数分块、同初始tail4、同q=.03991248545080898、旧warp reference=.04、同首轮λ1入口的全部15个物理raw控制、同1157合并后节点、M16/N512、tail N256/parts16/steps16、maxnodes6000和原1e−6/1e−7/2e−9门。

运行生成的原16维初始参数与首轮λ1入口逐值相等，初始16维尾H也逐值相等。口径是两次λ1入口相同：accepted λ=.02 的旧p乘旧pscale经新gauge重编码时，首个物理c从 .00021128347873463125 变为 .00021128347873463122（负1 ULP，绝对差2.710505431213761e−20），其余14个相同；这是首轮原restart已有的舍入，并非C²窗改动。profile和round settings的JSON对象相等；launcher只有三个输出文件路径改变，tail config只有traceFile输出路径改变。完整输入SHA（含必要的旧系数块 `6637680be24885749acace4d688299ade99249c0760558bf5dc7c42186202f22`）见执行记录。

新执行 session36328 已通过原restart并继续运行。此入口记录不写 solver_success，不借旧尾/旧prefix接受状态领取新端点；后续须原实际coupler完整返回才登记终态。

首次启动99034在记录字典重复 `scope` 键处明确exit1，发生于tail进程及solve_bvp之前。该源SHA、命令、完整输入和错误保留为工程来源；修复只改字典记录写法，随后在v2新目录运行，未覆盖首次执行证据，也不把启动错误称作数学失败。

复现命令与全部来源见 `scripts/resume_m3/circle_endpoint_c2_seed_entry_record.json`。新入口源为 `continue_m3_raw_circle_endpoint_c2_seed.py`、`couple_m3_raw_circle_endpoint_c2_seed.py` 和 `install_endpoint_c2_restart.py`；前两者由已登记端点入口独立派生，运行中不修改。原 checkpoint、系数数组和worker数据只在scratch中保留。
