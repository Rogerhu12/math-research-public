# 新输入：正确 h=k、Delta=0 的固定十七阶 lambda 覆盖

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。
**尚未执行。** 首次总预算 180 秒、4 GiB。
源 SHA256：4a8f1140c851838930c7b3992ff318ddda2b1f9ec8da90f08d46bd614749cd25；10330 字节。
建议 basename：
2026-11-28-unit211-h-equals-k-corrected-fixed-u-seventeen-lambda-cover-8542.py。

## 1. 只接正确的两条原曲线

准确范围为对称归一 $h_U=k_U$、$\Delta=0$，
$$
ABQ(1-Q)P_f\,bcP_{02}\ne0.
$$
$P_f=0$ 全支仍保留。这次不外推任何 W 的 $D\ne0$ 单位，
不使用旧错误 compact mean 或旧错误第二曲线。

原独立相容曲线 $P(\lambda,u)$ 已经实际完成，
$$
\deg_{\lambda,u}P=(28,3),
$$
规范参数 SHA256
8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c。
它只来自原 $\Delta,T_n$，真实运行
46025096446/job140594347573，不涉及被撤回的 $R_{\rm bad}$。

正确原 RWO 给出的另一条曲线为
$$
M_{\rm true}(\lambda,u),\qquad
\deg_{\lambda,u}M_{\rm true}=(110,14).
$$
其实际来源为 run46120122225/job140902587651，
双变量规范 SHA256
65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663。
全实际 source 4e80... 的 SHA256 为
3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33。

两曲线已证 QQ gcd 为一；本次不重算这个 gcd 或已成的
722 基点/后续原纤维计数结论。新目标是此前没有计算的
固定 $u$-Sylvester 行列式本身及其完整 QQ 因式覆盖。

## 2. 必要输入前缀的准确边界

唯一用来定义 $M_{\rm true}$ 的已有源码是
2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py。

截到以下唯一标记之前：
“# Reuse only the independent, already executed D/T curve P.”
前缀精确为 6055 字节，SHA256
09e0b44a9b6f244d0e2a11c1361b5382219aa5cad609efc3ae08fd370d318c7b。

这个必要前缀只再生正确 RWO、已证 $F_{61,17,9}$ 及
$M_{\rm true}$ 的定义，最后核上述 M 参数 SHA。这里必须从定义得到
新行列式的实际系数，不把它重记为一个新投影结论。
前缀不进入旧 P 读取、旧 P/M gcd、722 证明或旧分类尾部，
更不进入 dc888 的冻结 $z$ 结式。

它内部只调用正确 f33 的 5121 字节原 R/W/O 必要定义：
2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py，
全源 SHA256
2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2；
前缀 SHA256
325c32cb81f37b3f31affd4e98f01c39fcee75b2cc0eae1d9cbb079edaf6d078。

两层旧输出都被静默，只把它们作为输入定义。
所有嵌套 alarm/setitimer 被钳到本次原 180 秒绝对截止，
硬地址空间一直为 4 GiB。

## 3. 独立 P 只从历史终端临时读取

沿原工作流
invariant-subspace-8542-hk-corrected-delta-zero-q.yml
已有安排，用终端 git 从
ac40c96b0cfb3758fbf8bd380d18ca288a23601f
的
topics/invariant-subspace-problem/notes/2026-11-27-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover-receipt-8542.json
读到 runner 临时文件
isp-hk-independent-Delta-Tnum-legacy.json。

这里只匹配并在内存中解码 SHA 8af7... 的独立 P，
再逐字核其规范 SHA 和双次数。
历史文件名中的旧 “848” 不构成本次结论；
其中旧错误 M 从不解码，也不恢复其已撤回覆盖。
没有经工具搬运、打印或重新保存任何大系数载荷。

## 4. 固定十七阶新行列式与完整首项零面

将两输入仅乘非零 QQ 常数，使全部系数为本原整数，
并逐系数乘回原有理输入。记这样得到 $\widehat P,\widehat M$。

构造固定十七阶矩阵 $S$：前十四行依次是
$u^j\widehat P$，$0\le j<14$，后三行是
$u^j\widehat M$，$0\le j<3$，列按 $1,u,\ldots,u^{16}$。
新目标为
$$
R_{17}(\lambda)=\det S(\lambda). \tag{1}
$$
它与原 $\operatorname{Res}_u(P,M_{\rm true})$ 只差非零 QQ 常数。
每个共同有限根 $u_0$ 使
$$
S(\lambda)(1,u_0,\ldots,u_0^{16})^t=0. \tag{2}
$$
所以原点必有 $R_{17}(\lambda)=0$。
这一论证不倒任何 $u$ 首项；固定参数时 $u$ 次数下降、
两首项同为零等所有分支都保留。

源使用这一个固定矩阵的分式消去。每个 Bareiss 商必须真整除，
并实际验证“商乘前一主元等于原分子”。
它给出 $\mathbb Q[\lambda]$ 中完整的多项式行列式身份；
临时主元在某个 lambda 值为零不删除那条纤维。

无论算法中间如何选行主元，最终次数上界为
$$
\deg_\lambda R_{17}\le 28\cdot14+110\cdot3=722. \tag{3}
$$
若实际行列式为零，源明确不作新覆盖或排空结论；
若非零，先报告实际次数、字节数、SHA，再继续完整付单位剥除。

## 5. 仅允许的 lambda 支持

只从 (1) 剥去已独立证明不可能出现的纯 lambda 支持：
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\lambda,\quad2\lambda-1,\quad S_{\rm num},
$$
$$
S_{\rm num}=(2\lambda-1)(2\lambda^2-1),\qquad
S=S_{\rm num}/A. \tag{4}
$$

$A,B$ 是当前原值坐标图的单位；
$\lambda$ 来自非零 mean 的原 U-value atlas；
$2\lambda-1$ 引用独立347c真实原物理排除；
$S$ 引用已经逐份静核过的真实 S0 碰撞排除，不能借错误 compact 链。

旧 M 定义中已使用的 $u,u-1$ 原排除只属输入来源，
不意味着在此 lambda 结式中可以剥未知的额外投影因子。
不支付 $P_f=0$、任何新的 lambda 首项或新不可约支持。

每层 gcd 剥除都实际返回
$$
R_{17}=U_{\rm paid}R_{\rm rem}. \tag{5}
$$
归一首一仅除非零 QQ 常数。
随后完整 QQ factor，保留每个因子及原重数，并实际乘回 (5)。
最终平方自由乘积仅给共同根的必要覆盖；
原 $u,Q$、Gram 和个别原值都要在同一个完整常数域内继续返回，
不能以 lambda 候选有限当作碰撞支排空。

## 6. 归档与停止边界

此源只有一个新的实际数学目标 (1)。
保存实际阶段、每步精确除法数、QQ 因子次数/重数/规范 SHA、
真实运行参数及小回执；不输出大系数、encoded payload 或分片。

若180秒/4GiB先到，按最后完整阶段登记，不提预算、不重启，
也不把已经成功的必要输入再生冒充新结论。
所有未知因子和原首项零面仍完整保留。
