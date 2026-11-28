# W / f=u / t 非零：无均值头逆的四次权曲线与新原投影

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。
AI-assisted，GPT-6 Astra Pro。

这是整 t=0 返回之后的下一互补输入，现仅冻结源定义，尚未执行或派发。
自含源 2026-11-28-unit211-W-f-equals-u-t-nonzero-whole-original-projections-8542.py，
14529 字节，SHA256 5bc14c2eda09fe876d5c1bb659203d29aea8b0cf20b439920bcc8ed857e66770。
首次预算 180 秒 / 4 GiB，零依赖。没有任何旧 determinant/结式门。

## 1. 新的完整原坐标

沿当前原物理 W 图，仅加 $f=u,t\ne0$。
设
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=u((k+2)^2-2ek)/(kV_b),
$$
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2,\quad \delta=1-Q,\quad g=2\ell-1,
$$
$$
\widehat U=V_2-u,\qquad w=2V-(1+2\ell)u.
$$
原 $E_0$ 给
$$
x=u+\tfrac12+(V_2-u)w/(2M),\qquad
y=\tfrac12-uw/(2M).
$$
正确 $R_{\rm true}/t$ 在已付 $M$ 上准确解
$$
\boxed{t=2+2\widehat U w/M.}
$$
没有倒置 $V_2,\widehat U$ 或任何新的权头。
这只使用已声明的 $t\ne0$；并不把该式外推为原 $t=0$ 条件。

从同一点完整正确 Gram 构造，$E_1=EW$；
两个余均值都是 $w^2$ 的一次式。
令
$$
A=2\widehat U^2-\delta V_2,\quad B=g\delta V_2-2M,
$$
$$
R_0=u-1+(1-\ell)Q,\qquad
C=(u-\ell)\widehat U+u\ell\delta,\quad D_2=u\delta-C.
$$
完整身份为
$$
2M\delta EW=A w^2+MB,
$$
$$
M^2\delta EBo=\widehat U D_2w^2+M^2R_0.
$$
因此纯权原组合是
$$
F_u=AMR_0-B\widehat U D_2
 =AM\delta EBo-2\widehat U D_2\delta EW.
$$
全程没有倒 $A$ 或 $\widehat U D_2$，其共同头零支完整保留。

## 2. 整个四次权曲线

将 W 权代入，上式有准确因式恒等式
$$
F_u=\frac{e^3u^2(Q-1)\ell H}{V_b^3}\,K_{fu},
\qquad H=4ek-k^2-4k-8,
$$
其中
$$
\begin{aligned}
K_{fu}={}&-8k^2e^4+(32k+16k^2+6k^3)e^3\\
&-(32+32k+16k^2+4k^3+k^4)e^2\\
&-(16k+18k^2+7k^3+k^4)e\\
&+16+20k+8k^2+k^3.
\end{aligned}
$$
所有外因子在当前 W 原域已付。因此 $K_{fu}=0$ 是完整原必要式。
它有 17 项、双次数 $(4,4)$、总次数 6，
$e^4$ 首项为 $-8k^2$，已是原单位。

上述纯权乘法已经有独立小整数多项式展开，0.039 秒全乘回；
新完整原均值及后续 $N/P$ 源尚未执行。
不把前者冒充后者的实际返回。
本源会从原 Gram 返回所有身份，并只将必要的原小参数定义留在源中。

## 3. 保全部 w 头零的完整原 N/P

在同一个 $(x,y,t)$ 上恢复原 $\lambda,T$，构成原 $N_1,NS,PS$。
保完整 $EW,EBo$；全部是至多 $w$ 三次的原式。
每个有理式都完整检查分母，只删除已付纯权内容并乘回。

先计算六个新的固定 w-Sylvester：
$$
\operatorname{Res}_w(EW,N_1),\
\operatorname{Res}_w(EW,NS),\
\operatorname{Res}_w(EW,PS),
$$
以及把第一行改为 $EBo$ 的另三条。
每个固定矩阵的完整多项式行列式由精确 Bareiss 商积返回。
任意原共同 $w$ 都使这些行列式为零，
所以所有 $w$ 头同时降次、甚至一条均值整式为零的支都被包含。
源从不以均值平方头来约化 $w$。

## 4. 新的固定 e 投影与真实剩余范围

六条纯权必要式记 $R_0,\ldots,R_5$。
这里临时沿用 $R_j$ 作为枚举名，区别第 1 节的权表达式 $R_0$。

先取 $\gcd(K_{fu},R_0,\ldots,R_5)$，只判断是否存在共同曲线：
非恒定时保整个共同曲线，不宣称有限或空。
恒定时，$K_{fu}$ 的 $e$ 次数为 4、没有垂直 k 内容，
故它至多有四个不同曲线分量。
对每一分量，$\sum_{j=0}^5 c^jR_j$ 至多有五个坏有理常数 $c$。
因此固定 $c=0,\ldots,21$ 中至少有两个与整 $K_{fu}$ 不共曲线。

源选前两个实际满足这一条件的原线性组合，分别计算
固定 $\operatorname{Res}_e(K_{fu},\sum c^jR_j)$。
多变量 gcd1 在这里仅支付“无共同曲线”的投影前提，
从来不是排空依据。

两条真正一元必要式只删除已付 $k,k+1,k+2,k+4$，
随后完整 QQ Bézout 乘回。
仅当实际 gcd 为非零常数，才排整个 $f=u,t\ne0$ 图；
否则保完整一元因式与重数，继续原有限返回。
所有 e 首项零由固定 Sylvester 保留，临时计算主元不支付物理单位。

这与已成 $t=0$ 的 F7、F12 和两个常数域是不同数学输入。
既有 t0 门不在依赖或执行路径中。
