# R182 实际有符号场的 native 与完整 Arb 消费

状态：**已证公式的实际消费；局部连续盒完成，没有全域解证书。**

## 实际对象与输入

本组实际输入为 notes/2026-11-12-fd2d-signed-trace-local-01-warm.npz，
137021 B，SHA256 b7d2ae3350926666cb25d634bbb14aa49a3eb6b04a5a07f9657a0fca90095626。
真正的结构来源是 34 接受态 b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f，
而不是将新数组交给旧 positive-trace schema 解码。

新准确 profile 包为 notes/2026-11-12-fd2d-metric-signed-warm-accurate-profile-rebind-01-packet.json.gz，
SHA256 a8df9aef4da79c535510d9b8b140a6d553640bac4c92a474737b16a6db055d8b。
该包显式绑定新归档及实际七个 profile 参数；已有准确 base 积分直接复用，没有重算积分，也没有把旧参数借给新字段。

新源码：

- scripts/fd2d_gc_signed_trace_archive_native.py，13900 B，SHA256 2e889c83edf4cd72a7089b80ccf64c53d00fe9ff7b3c30d86e44cc0799803ac5。
- scripts/fd2d_gc_signed_trace_complete_arb.py，14833 B，SHA256 0bc513970a7be8eaf27b59b8d3f90525e87d0555c3006aa50658e84a5d0c1c32。
- scripts/fd2d-metric-signed-trace-native-arb-check-v2.py，8170 B，SHA256 e1ce2a06ddb15c2946ca6cf425f6ef9a6ceb7d366e667e340a98aec979eb1ce5。

SignedTraceArchiveNativeField 的 schema 为
fd2d-R182-actual-signed-disjoint-trace-archive-native-v1。
SignedTraceAccurateDomainFieldArb 的 schema 为
fd2d-R182-signed-complete-accurate-domain-Arb-v1。

前者是实际保存定义的 binary64 求值器；后者使用 R171/R175 准确 profile、
R173 完整 affine/atlas/raw 公式及 R172 准确末格定义。
两个对象的点差只作浮点求值诊断，不能用作全域误差证明。

## 完整新表示的绑定

新归档必须明确声明
ruling_atlas_coast_Gauss_l_and_signed_disjoint_traces_v1。
signed_trace_definition 是全体有符号窗口定义；
positive_trace_definition 必须显式等于它的别名。
原末端正迹单独保存在 original_terminal_definition 中。

只有真实旧 b075 归档进入冻结旧结构构造器。随后核对固定候选、实际网格、
atlas/coast/seed 定义、计数与 supports；新 raw、中央参数、tail 参数和 profile
参数全部从新归档读取，并重建这些参数依赖的对象及 plain-lifting view。
当前严格绑定 131 个保存节点、中央 31、tail 16、profile 7，共 54 参数。
未来增加 profile 列需要新的实际布局和准确 packet，当前 J7 证包不能自动覆盖新增列。

新读者按归档显式窗口及迹符号读取，允许声明的窗口子集。
窗口端点按保存的准确 dyadic 数处理，支持互不相交且与 coast/原末窗分开。
可删除 trace gauge 依据完整 P1 帽支撑重算，不能仅因某节点在平台而删除其帽。

tail 使用 R170 八段局部 Bernstein 域。global control 可以为负，但当前实际
16 controls 的准确 certificate 必须与归档完全一致。旧 controls 的证书不能
给新 controls 使用。当前函数上界仍是 $6/5$。

## 有符号 jet 的准确恒等式

令 $S=(n,m,l)$、$d=n-l$、$h=\sqrt{d^2+4m^2+4K}$。
迹符号 $\sigma\in\{-1,1\}$ 的映射为

$$
\mathcal P_{\sigma,w}(S)=
\left(n+\frac w2(\sigma h-n-l),\
m,\
l+\frac w2(\sigma h-n-l)\right).
$$

正号复用冻结 R155 jet。负号用

$$
\mathcal P_{-,w}(S)=-\mathcal P_{+,w}(-S).
$$

证明：$(-n+l)^2+4(-m)^2+4K=h^2$；展开右边即左边。
在存在的变量上求导，同一恒等式保留全部值、固定 $\xi$ 的 $s$ 导数、
$\xi$、$\xi\xi$ 和 $s\xi$ 五个 jet。$m$ 及其导数两次取负后保持原值，
而 $K$ 始终不取负。

窗口为准确剪裁五次 smoothstep 的乘积

$$
w(s)=S_5((s-A)/(B-A))\,S_5((D-s)/(D-C)).
$$

权重导数保留两项，不能遗漏 falling 项。
请求径向 jet 时，在真实活动区域取

$$
K_s=-a_{sss}/a+a_{ss}a_s/a^2 .
$$

准确层从 R171/R175 的实际 phase/bump 表达式包围这些量。
这是实际 jet 的计算需求，没有新增全曲面 $C^3$ 完成门。
新增窗的活动连续盒必须真正得到 $K>0$；不以采样正值替代，宽盒不足则 unresolved。
原末窗保持自己的非负 $K$ 与正迹规则。

## 完整材料漂移与连接 forcing

设材料角 $u=U(s,\xi)$，则

$$
\partial_s|_u=\partial_s|_\xi-(U_s/U_\xi)\partial_\xi,
\qquad
\partial_u=U_\xi^{-1}\partial_\xi .
$$

用真正的材料导数定义

$$
G=nl-m^2+a_{ss}/a,\qquad
R_n=n_s-m_u/a-(a_s/a)(l-n),\qquad
R_m=m_s-l_u/a+2(a_s/a)m .
$$

消费者输出 R119 的全部三个 forcing 分量

$$
H=(-aR_n,\ aR_m,\ -aG).
$$

因此不能把 native 的固定计算角 n_x/m_x 直接当材料 n_s/m_s。
角二阶和混合导数也保留真实 $U_\xi,U_{\xi\xi},U_{s\xi}$。
准确 atlas 沿 R173 的完整语义，旧浮点 endpoint shortcut 不变成新数学定义。

## 准确 cut 的作用域

新增窗在整个最后 P1 单元上恒零。新明确构造器可复用 R172 已证末格公式

$$
C(\sigma(s))+\eta(\sigma(s))T(a(s),u),
$$

然后用物理 $s$ 的准确 $K(s)$ 作原末端正迹。
$\sigma$ 只用于旧 raw 与 scalar weight，tail 半径仍为 $a(s)$。
准确 tail 常数为 $4/5,17/50,23/50$，实际 16 个 dyadic controls 保留。

准确 cut 仅返回值、角一阶、角二阶；径向及混合 II jet 为 None。
没有把 cut bypass 解释成 $E_s=0$。
一般 cut-touch forcing 和实际 posterior 尚须相应单侧界及累计，不由本次角查询自动支付。

## 实际执行及结果

checker 01 在首点准确消费后，因诊断误取 U_s 键而真 exit 1；
旧 native 的接口名实际是 U_x。失败源、报告、receipt 保留。
数学读者两份源码未改；另名 v2 仅修诊断字段名。

v2 实际 session 33385，initial chunk b7acc9，final chunk 7d3ea2，
自然 exit 0，内部 0.368107162 秒，峰 RSS 97300 KiB。

两个实际非零点：

| 点 | $s$ | $\xi$（弧度） | $\Delta n$ 显示值 | $|H|$ 上界显示值 |
|---|---:|---:|---:|---:|
| middle rising | $363/400$ | $7/20$ | $0.00739640044215$ | $0.91100571501$ |
| late falling | $2887/2000$ | $1/5$ | $-0.02938819193110$ | $26.04725200364$ |

报告保存准确 dyadic 端点；表中仅显示数值。
全部 30 个 native jet 的 absolute/scaled 最大点差为
$1.534773\times10^{-12}$ / $1.303402\times10^{-13}$，只是数值求值诊断。

正面积连续盒位于实际 cell 82：

$$
s\in[363/400-2^{-27},363/400+2^{-27}],\qquad
\xi\in[7/20-2^{-24},7/20+2^{-24}].
$$

盒中真实包围给出向外放宽的十进制界：

$$
\begin{aligned}
1.0656641648&<K<1.0656650058,\\
0.2292305344&<U_\xi<0.2292308483,\\
0.0253612460&<U_s<0.0253615249,\\
-0.020215941&<G<-0.020200864,\\
0.7963497277&<R_n<0.7970331735,\\
-0.1837402214&<R_m<-0.1833931205,\\
|H|&<0.91141999048.
\end{aligned}
$$

它实际消费了非零 $U_s$ 与 $w_s$。
真实准确 cut 在 $u=1/5$ 的角两 jet 完成，且没有赋径向 II jet。
输入归档最后再次核得未变。这些实际缺陷仍明显，特别是晚段点；
没有将 reader 通过当成方程解通过。

## 输出身份及可重做范围

共同 stem：
notes/2026-11-12-fd2d-metric-signed-warm-native-arb-R182-02

- native-definition.json：71692 B，SHA256 484a05f949b19e6eec8195caa7520dbafbdcd3e32dc80100741b751ffb4c7ebc。
- interval-definition.json.gz：30541 B，SHA256 25964d645aef31b5d3b657c91f190460f65a55291a204f55495df432b66c0630。
- report.json：78247 B，SHA256 bb710280f62807b382d16177debdfd1c5ff9c7da2c93f3b6610c0774b938fdf3。

以 python-flint 0.9.0 运行 checker v2，参数为 --field（b7 warm）、
--origin（b075）、--foundation-definition（已闭30 native定义）、
--profile-packet（上述新绑定包）、--profile-sha256（a8df…）、
--out-prefix（另名）。不会运行 F/J、BVP 或 body。

准确全域 R125 remainder、累加、初始相容和 actual body posterior 本组未付。
一般 ExactNormalizedCellPrimitive 可按新字段绑定；限制旧 schema 的
R180/R178 专用入口需要显式适配，不能仅换字符串后宣称已消费。

本说明是在 executor 暂时 unavailable 后，根据刚刚真实输出和已读源码写成的新文本。
它不宣称失联后的文件可用性；上面运行结论均来自失联前已自然退出的实际工具结果。
