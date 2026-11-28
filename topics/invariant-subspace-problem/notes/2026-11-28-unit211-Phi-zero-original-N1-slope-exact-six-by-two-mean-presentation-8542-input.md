# Phi 原 N1 斜率坐标：完整六行两列原呈示的新输入

日期：2026-11-28（Asia/Taipei）  
状态：尚未执行；120 秒、1 GiB，包含必要构造前缀。只输出小回执，不保存可重算系数。

## 1. 同一原范围

范围为当前一般 unit211 的 $\Phi=0,D\ne0$ 原图。这里整第一二次头已经由
[整 H1 原排除](../results/R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md)
支付。所有旧原权单位照旧；$u+Q-1$ 引用
[整个一般 Q=1-u 原排除](../results/R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)，
$2\ell-3$ 仅引用当前 Phi 图的
[完整例外有序权图与 B/C 交换](../results/R150-appendix-unit211-Phi-zero-exceptional-weight-chart-complete-original-exclusion.md)。
不把这些限定结论搬到 $D=0$ 碰撞图。

记 $q_R,q_W,q_O,q_N$ 为已付的三个完整原均值和完整原 $N_1$。前三式的二次头矩阵为 $H$；其真实规则写为
$$
(T^2,Tz,z^2)^t=\mathcal R(1,T,z)^t+H^{-1}(q_R,q_W,q_O)^t.
$$
记第四式的二次头行为 $h_N$，则完整恒等式为
$$
q_N=n+h_NH^{-1}(q_R,q_W,q_O)^t,
\qquad n=p_0+p_1T+p_2z.
$$
真实次数界是 $\deg_\lambda p_0\le2$、$\deg_\lambda p_1,\deg_\lambda p_2\le1$。

## 2. 新权斜率与完整坐标变化

写
$$
p_1=a\lambda+b,\qquad p_2=c\lambda+d,\qquad
\Delta_N=ad-bc=ap_2-cp_1.
$$
其中 $a,b,c,d$ 只含权参数。整个 $\Delta_N=0$ 权面保留。本源不以函数域非零当它处处为单位。

在 $\Delta_N\ne0$ 的明确补图，令
$$
\mathcal Z=aT+cz,\qquad \nu=p_0+p_1T+p_2z.
$$
这是真实可逆仿射变化：
$$
T=\frac{p_2\mathcal Z-c\nu+cp_0}{\Delta_N},\qquad
z=\frac{-p_1\mathcal Z+a\nu-ap_0}{\Delta_N}.
$$
由于 $\nu=n$ 属于原四式理想，且 $q_N=n+h_NH^{-1}(q_R,q_W,q_O)^t$，原理想恰等于 $(n,q_R,q_W,q_O)$。因此消去 $\nu$ 后，原四式商严格同构于三个真正代入后的 $\mathcal Z$ 二次式 $\widetilde q_R,\widetilde q_W,\widetilde q_O$ 的商；不是仅在原点上成立的必要条件。

## 3. 首一二次与精确六行两列呈示

令 $v=(1,T,z)^t$。由真实平方规则，
$$
\mathcal Z^2-rv=(a^2,2ac,c^2)H^{-1}(q_R,q_W,q_O)^t.
$$
在 $\nu=0$ 代入上式，得到
$$
P=\mathcal Z^2-\beta_1\mathcal Z-\beta_0
 =\sum_{i=R,W,O}\sigma_i\widetilde q_i,
\qquad
\sigma=(a^2,2ac,c^2)H^{-1},
$$
其中 $\deg_\lambda\beta_0\le3$、$\deg_\lambda\beta_1\le2$。本源直接乘回所有三个 $\mathcal Z$ 系数，并乘回 $q_N$ 在三个已代入均值中的完整表示。

若 $\widetilde q_i=q_{i,0}+q_{i,1}\mathcal Z+q_{i,2}\mathcal Z^2$，记
$$
r_i=(q_{i,0}+q_{i,2}\beta_0,\ q_{i,1}+q_{i,2}\beta_1).
$$
则 $\widetilde q_i=r_i(1,\mathcal Z)^t+q_{i,2}P$，故
$$
(\widetilde q_R,\widetilde q_W,\widetilde q_O)
=(P,r_R(1,\mathcal Z)^t,r_W(1,\mathcal Z)^t,r_O(1,\mathcal Z)^t).
$$
首一二次环境在权环加 $\lambda$ 上自由秩二。在这个环境中
$$
(r_0,r_1)\mathcal Z=(r_1\beta_0,\ r_0+r_1\beta_1).
$$
每个子行再次乘 $\mathcal Z$ 恰等于 $\beta_1$ 倍子行加 $\beta_0$ 倍母行。因此整个原四式商有精确的六行两列模呈示
$$
r_R,\ \mathcal Zr_R,\ r_W,\ \mathcal Zr_W,\ r_O,\ \mathcal Zr_O.
$$
只有首一二次环境被称为自由；原商不假定自由。全部 $\lambda=0$ 纤维仍包含。

## 4. 新的小原标量目标

对每个完整原均值的行 $r_i$ 及其真实子行 $\mathcal Zr_i$，源作一个固定 $2\times2$ 常数目标。两行仅乘补图已付权单位清分母。若两乘子有共同因子，只从这两个真实乘子中整除；随后完整返回两个列积，得到 $(P_i(\lambda),0)$。这保留该共同因子的整个零集，因为新的多项式乘子自身给出原理想组合。

最终只剥旧权单位和明确的 $\Delta_N$ 补图单位。任何未付权内容、$\lambda$ 首项零集、零标量或退化行都准确保留。原 $D$ 不被倒置；这里尚未加入所有个别原值式，也不声称整个 Phi 空。所得标量是新的真实原理想输入，不用它替代尚未支付的全值返回。

## 5. 身份与依赖

建议源文件：

`2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`

源 blob `e7973898af760437428eea7ccc9aa8552b9b2db5`，12550 字节，SHA256

`c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332`。

唯一源码依赖：

`2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，

SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`。只取旧 D cofactor 之前的 7097 字节必要原规则，前缀 SHA256 `9467955925e4f6bd05aaf74c5d8fb7e747a03c0a5119fb17ee2b87e7703a701b`。可用环境变量 `ISP_PHI_FIRST_HEAD_RULE_SOURCE` 指定路径，默认同目录 basename。

嵌套 `alarm` 和 `setitimer` 均被钳制到本源最初的绝对 120 秒截止。不重放旧 P6/P9、旧弱 Popov、旧 Gaussian、旧范数或整 Gram 门。新原式及其来源由源码定义；输出仅次数、项数、哈希、精确乘回状态和全部未付范围。
