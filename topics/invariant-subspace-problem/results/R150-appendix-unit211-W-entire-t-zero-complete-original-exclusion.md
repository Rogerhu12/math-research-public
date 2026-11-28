# W：整个 t=0 原分支的完整排除

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。
AI-assisted，GPT-6 Astra Pro。

## 1. 结论

在当前已经严格界定的物理一般 LS、$\Delta=0,W=0$ 原图，
整个 $t=0$ 分支为空。因此后续在这个完整当前 W 原图可以支付 $t$，
不再保留一个未闭 $t=0$ 例外。

结论只沿该图原有的单位和 $D\ne0$ 范围；
不外推到辅助 $D=0$ 双数族、一般 Phi 图或未经归一的其它原图。
本篇也没有宣称整个 W 排空或一般 ISP 完成。

本篇合成三个已实际完成的原结论：

1. [t=0 的原均值两分支及整个 V2=0 排除](R150-appendix-unit211-W-t-zero-mean-branches-and-V2-zero-complete-original-exclusion.md)；
2. [完整三个固定原投影与 F12 覆盖](R150-appendix-unit211-W-t-zero-original-F12-complete-parameter-cover.md)；
3. 本次两个完整 QQ 二次常数域的原 $e$ 返回。

没有为合成重新计算前两项。

## 2. 全图覆盖没有遗漏分支

正确原 jet 乘法的均值身份给
$$
t=0\quad\Longrightarrow\quad(f-u)(V-f)=0.
$$
$V=f$ 支已由完整原均值组合排除；
整个更一般的 $A_1=t=0$ 原 jet 恒等式也独立给 $D=0$，
与当前物理图矛盾。这里任何一个完整已成来源即可，不重复计数。

剩余 $f=u$ 中，整个 $V_2=0$ 已由原 $N_1,NS,PS$ 的两列
QQ Bézout 单位组合排除。在 $V_2\ne0$ 图，令
$$
g=2\ell-1,\quad M=\ell V_2-u^2,\quad J_0=V_2-uQ,\quad
w=-gJ_0/V_2.
$$
于是
$$
x=u+\tfrac12+(V_2-u)w/(2M),\quad
y=\tfrac12-uw/(2M),\quad f=u,\quad t=0.
$$
所有 $\lambda,T$ 与原单点条件都来自这个同一点的正确 Gram。

完整三个固定 $e$ 结式和 QQ Bézout 已给
$$
F_{12}=\phi_a^2\phi_b^4=0,\qquad
\phi_a=k^2-2k-16,\quad\phi_b=k^2+8k+8.
$$
没有删除两个二次因子的任何根或其原重数。

## 3. 两个完整常数域的真实返回

本次只重建上述已成源中 8038 字节的必要原标量构造前缀，
在首个因式分解定义之前截断；旧三结式、QQ 因式与参数 xgcd 尾
一概不运行。

随后分别进入
$$
K_a=\mathbb Q[k]/(\phi_a),\qquad K_b=\mathbb Q[k]/(\phi_b).
$$
判别式为 $68,32$，都非平方。程序按 $(1,k)$ 正规表示计算整个域，
并对每一个实际逆完成左右乘回；没有选一个数值根。

在每个完整域，四条同点原多项式
$$
F_7,\quad N_*,\quad S_*,\quad P_*
$$
先真实专门化，再取它们实际的 $e$ 次数。
本次均为 $7,13,16,22$。程序逐次 Euclid 并累积四条原行的
完整 Bézout 来源，每一个商余与最后组合都乘回。

### 3.1 整个 phi_a 域

四行原 gcd 为一条首一 $e$ 一次式 $G_a$，
定义 SHA256 为
42b9582bbaf9c1aaea0836b7d9fd2c6777f69be520302cde613a0a26bf249437。

精确原返回得到
$$
L_{\rm half}=0\quad\text{于 }K_a[e]/(G_a),
$$
并且有完整
$$
G_a=\sum_i a_iP_i
$$
的原四行来源。因此
$$
L_{\rm half}\in(F_7,N_*,S_*,P_*)\subset K_a[e].
$$
当前整个 $L_{\rm half}=0$ 已由
[整 Lhalf 原排除](R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)
关闭，故 $L_{\rm half}$ 是实际原单位。
整个 $\phi_a$ 域遂无原解。

本次只用这一原单位删除一次；没有用原 D 的模零或选择一条 e 根。

### 3.2 整个 phi_b 域

四行原 gcd 为首一二次式 $G_b$，
定义 SHA256 为
61d33576db50bc7755abda82b774a379f66d4d07cf75011d9b93a42edacde580。

原单位 $u=e+1$ 反复 gcd 两次移尽整个 gcd，
并且程序必须实际返回
$$
u^2=0\quad\text{于 }K_b[e]/(G_b).
$$
连同完整四行 Bézout，得到
$$
u^2\in(F_7,N_*,S_*,P_*).
$$
原孤立均值图已有 $u\ne0$，所以整个 $\phi_b$ 域也无原解。

这里保留了二次 gcd 的幂零信息，不是只检查一个简单 e 点。

## 4. 原平方、四次幂与全部零纤维

原投影为 $\phi_a^2\phi_b^4$，而本次先算模 $\phi_a,\phi_b$。
这不会遗漏原幂零层：

在原 $\phi^m$ 层，$J=(\phi)$ 为幂零理想；
上述完整原单位返回给 $I+J=R$。
若 $1=i+j$，$j^m=0$，则 $1-j$ 是单位，所以 $I=R$。
因此原 $\phi_a^2$ 和 $\phi_b^4$ 全部层同时被排除。
两个二次因子互素，CRT 覆盖完整 $F_{12}$。

也可先使用 $F_7$ 的已付 $e^7$ 首项 $k^4$，
得到完整有限 $e$ 模型，再作相同的幂零提升。
各原权单位的局部化只删除该 Artin 环的分量；
本次没有把局部化当作无条件保持有限自由的依据。

三个旧固定 Sylvester 本已包含所有有限 $e$ 首项零纤维，
本次又在完整域中先专门化再做实际次数运算。
加上原 $V=f$、$V_2=0$ 的完整排除，
整个当前物理 W 的 $t=0$ 已全部关闭。

## 5. 实际执行与可再生身份

[唯一新源](../notes/2026-11-28-unit211-W-t-zero-F12-two-complete-quadratic-original-fibers-8542.py)
blob fe702d2a94c7823cfbb572bac730167009d78aff；
9614 字节，SHA256
231857b9f6d7c6325fb23394958abd644aac743394c210e2f653502a7a5f0d12。

实际 run 46108879333，job 140867728115：

- source 与实际 pull 均为 18cf6029df8b697c760743662b8d1df69490f6ae；
- pull 时间 2026-11-28 04:43:59.879874 UTC，两 README 无变；
- driver 0.220794245 秒，RSS 40548 KiB，内层退出码 0；
- 数学末阶段 0.163134770 秒，源内 RSS 39964 KiB；
- 92 次二次域双逆返回、65 次精确多项式商余返回、
  25 次完整 Bézout 返回、3 次原单位幂的模乘法返回；
- stdout 5558 字节，SHA256
  c9d80c94a7b57079e1acdc5a11ebdfd731e1aac38104b6b703704b743e04ead4。

[小回执](../notes/2026-11-28-unit211-W-entire-t-zero-complete-original-exclusion-receipt-8542.json)
保完整真实阶段与参数定义，不存可重算矩阵或系数载荷。
后续转整个 $t\ne0$ 的新原输入；旧 t0 结式与两个整常数域均不重跑。
