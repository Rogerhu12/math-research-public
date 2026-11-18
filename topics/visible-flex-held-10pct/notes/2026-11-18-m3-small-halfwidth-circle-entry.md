# 小半宽精确圆弧的实际联合入口

状态：**新的物理设计已启动，尚无接受结论**。前一条 $a=.21$ 二阶核心正性界入口已完整失败；本条按预声明的五半宽初猜证据，取 $\lambda=1,a=.01$，保持原其余设置和全部门，从原 raw $\lambda=.02$/M16 的有限接受输入重新起步。没有使用失败态的大控制。

## 明确改变的对象

相对已结束的 $a=.21$ 入口，只把精确圆弧保护半宽改为 $.01$。保持

$$
q=.03991248545080898,\quad b_p=.32,\quad b_c=.4,\quad n=3,\quad\eta=0,
$$

以及原 mean/primary 矩条件、全部 15 个物理控制初值、角图 $e=.32$、flat profile、ShortBridge、真实物理尾、M16、512 前缀角节点、1024 审计角节点、tail parts16/steps16/depth8/256 点求积。

核心与控制基都按新半宽完整重建；保持控制数值不等于保持控制函数。`circle_halfwidth_a001_entry_record.json` 引用五点探针中同一个新 $2\times2$ Gram 和完整基矩阵哈希。当前实际初始参数、15 个物理控制、16 个尾高度 $H$ 相对上一 $a=.21$ 入口均已核 **binary64 字节相同**，profile 相同，tail 配置只换 trace 路径；共享 C² 修复元数据也相同。相对最早接受 raw CP 的首个控制 $-1$ ULP 规范往返已另行登记，没有因本半宽变化增加。

新的 owned coupler 仅放开明确声明的半宽设计变化，仍要求 $0<a\le.21$ 和 $\lambda=1$，保留中心/对称/锁主频核验。原 Frenet/Newton/Jacobian、真实 DN、$2\times10^{-9}$ 尾停止门、核心 $10^{-5}$ floor、32768 网格上限及已审二阶充分界均不变。未装右预条件或新的线性幅值预测器。

## 实际启动与来源

执行句柄 **19739**，2026-11-18 00:14 UTC 启动；已有 `observed_running` 资源记录和完整初始化输出。指定径向点 1143，合并断点后初始 1157 点，上限仍为 6000。原 `observe_command_live.py` 仅记录 stdout/资源/真实退出，不改变求解。

目录：`m3_work/beta4625-q039912-raw-lam1-a001-b032-w040-m16-c2guard`。初值来源仍为
`beta4625-q040-raw-lam002-fixed-m16-neighbor/seed.json.gz`（SHA `6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e`）及其原 tail 4（SHA `220fab12b9d25daa0f23c91f00945321b9c447813b3120281aa00d2793dd1910`）；输入的原完整 metric 未过门这一事实不变。

完整启动命令、初始参数/H、CP 系数分块、所有 source/input SHA 和 observer 命令都在紧凑入口记录中。新的两个源为：

- `couple_m3_raw_circle_halfwidth_c2_guard.py`，SHA `cccda78b68acc6d917d83a33b0583c4e3f219b48d26e2ed5539e0a882850000f`。
- `continue_m3_raw_circle_halfwidth_c2_guard.py`，SHA `e50590ef410afbd9397a76521f492d0287b777e9c9bb5e6aeeca7cf1f336c321`。

这是一条新的物理核心设计，不能称为相同整度量的加密。尚待完整前缀、新末端 $H$ 的实际尾、完整 metric 和接缝审计；若得到可用圆弧锚点，再明确向目标 $a=.21$ 续接。小半宽不能移用 $a=.21$ 的握持见证或 10% 比例。
