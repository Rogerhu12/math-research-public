# R150 附录：单位 2+1+1 的非零孤立点均值、单位基点均值图排除半比例及全部 jet 除数

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

**状态：本条完整范围已证明。** 在原单位 $2+1+1$ 加孤立零点的长度五分支，保不同、非相反且非零的两基点配对、非零最高基值 $P_0$ 和非零孤立点均值 $m$。共同规范 $p+q=2$ 后，若基点均值 $u=bp+cq=1$，则总单点权 $\ell=b+c$ 不能为零，比例 $\lambda=m/u_0$ 不能为 $1/2$，且原一阶 jet 用来解交叉配对的系数处处非零。这里的 $u=1$ 在规范前就是 $2(bp+cq)=p+q$。本稿不宣称一般 $u$ 或本图的其余比例已经排空。

## 1. 同一原系统及非零比例

沿用[原单位 2+1+1 模型](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)及[共同对称规范](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-singular-faces-exclusion.md)。记
$$
p=1-\kappa,\quad q=1+\kappa,\quad Q=pq=1-\kappa^2,
\qquad Q(Q-1)\ne0,
$$
$$
\ell=b+c,\quad u=bp+cq,\quad a=1-\ell,\quad
b=\frac{\ell q-u}{2\kappa},\quad c=\frac{u-\ell p}{2\kappa}.
$$
全部配对和零点列共同缩放，原 mean、最高式及第二梯度按各自齐次次数保持。形式关系 $\kappa^2=1-Q$ 保两种标号与两个根。

原活跃代数、Gram、零点配对列为
$$
\tau(x)=a x_0+x_1+b x_B+c x_C,\qquad
K_B=\begin{pmatrix}0&0&p&q\\0&A_1&r&s\\p&r&0&t\\q&s&t&0\end{pmatrix},
$$
$$
U=(u_0,u_1,u_B,u_C),\qquad m=\tau(U),\qquad
\widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix},\quad
\operatorname{rank}\widehat K\ge4.
\tag{1.1}
$$
记同一原 $P,N$ 的值和一阶 jet 为 $P_i,N_i$。由原最高式和第二梯度，
$$
P_0=-u_0^3\ne0,\quad N_0=-mu_0^2,\quad
P_1=-3u_0^2u_1,\quad N_1=-2mu_0u_1.
$$
所以本稿 $m\ne0$ 等价于
$$
\lambda:=\frac{N_0}{P_0}=\frac{m}{u_0}\ne0,
\qquad 3N_1-2\lambda P_1=0.
\tag{1.2}
$$
另由同一原零点 mean、最高式，
$$
\tau(U^2)=2m^2,\qquad \tau(U^3)=4m^3.
$$
因此令
$$
\overline N=aN_0+N_1+bN_B+cN_C,\quad
\overline P=aP_0+P_1+bP_B+cP_C,
$$
就有必须保留的无除法条件
$$
S=\overline P-2\overline N=0,\qquad
\overline N-2\lambda^3P_0=0.
\tag{1.3}
$$
这些都只是原解的必要式；后文不将它们的抽象解当作物理存在性。

## 2. $E_0=0,N_0=\lambda P_0$ 的全局原图

令 $d=D_K1$、$f=\tau(d)/2$、$x=d_B$、$y=d_C$、$g=bc\,t$，并置 $V=2u-\ell Q$。从原 Frobenius 乘法直接得到
$$
W_1=bp x+cq y=V/2-u^2+2fu,
$$
$$
W_2=bp^2x+cq^2y=uV-2u^3+f(V+2u^2)-Qg+2\lambda P_0.
\tag{2.1}
$$
所以
$$
x=\frac{qW_1-W_2}{bp(q-p)},\qquad
y=\frac{W_2-pW_1}{cq(q-p)},
$$
$$
t=\frac{g}{bc},\quad r=x-ap-ct,\quad s=y-aq-bt,\quad
A_1=2f-2bx-2cy+2g.
\tag{2.2}
$$
这里只除原非零的 $bc,p,q,q-p$；相对于零 $m$ 图，$W_2$ 中保留准确的 $2\lambda P_0$。

从现在起令 $u=1$。原权重与最高值为
$$
D=\ell^2Q-2\ell+1,\qquad bc=\frac{D}{4(Q-1)}\ne0,
\qquad P_0=\frac{Q(\ell-1)}2\ne0.
\tag{2.3}
$$
故先验非零乘积为
$$
K_0=Q(Q-1)(\ell-1)D\lambda.
\tag{2.4}
$$
代回同一原六条必要式
$$
E_1,\ E_B+E_C,\ (E_B-E_C)/\kappa,
\ 3N_1-2\lambda P_1,\ S,\ \overline N-2\lambda^3P_0.
\tag{2.5}
$$
它们在形式二次代数内都是偶式。取各约分分子，反复仅除与 (2.4) 的 gcd，并按字典序 $(f,g,\ell,Q,\lambda)$ 作有理数首一化，定义六个确定多项式 $M_0,\ldots,M_5$。源码直接从原乘法重建此过程，不读取消元数组。

原 jet 多项式 $C=M_3$ 对 g 为一次式。置
$$
\Delta_g=2f+2Q\ell\lambda-Q\ell-2\lambda,
\qquad f_*=Q\ell(1/2-\lambda)+\lambda.
$$
准确身份为
$$
\frac{\partial C}{\partial g}=-\frac{Q\ell\Delta_g}{2},
\qquad
C(f_*,g)=Q^2\ell^2\lambda(2\lambda-1)D.
\tag{2.6}
$$
下两节先独立支付两个系数零面，再处理整个半比例。

## 3. $\ell=0$ 的整个非零比例图为空

在 $\ell=0$，原 jet 分子准确为
$$
M_3=2(f-\lambda)^2,
$$
所以 $f=\lambda$。代回原第三条 mean 分子，得 $M_2=2Qg^2$，故 $g=0$。第二条 mean 此时是
$$
M_1=\frac Q2(2\lambda^2-2\lambda+1).
$$
而同一原 $S$ 分子 $M_4$ 在 $f=\lambda,g=0$ 后，模 $2\lambda^2-2\lambda+1$ 的余式准确为 $Q\lambda$，由 (2.4) 非零，矛盾。

因此后文可使用 $\ell\ne0$。它没有被从一般图中直接删去。

## 4. $\Delta_g=0$ 全部归到半比例的唯一顶点

若 $\Delta_g=0$，则 $f=f_*$。由 (2.6) 和已付 $Q\ell\lambda D\ne0$，必有
$$
\lambda=f=\frac12.
\tag{4.1}
$$
将 (4.1) 代回原六式，取分子后仅去除已非零的 $Q(Q-1)\ell(\ell-1)D$。其 $\mathbb Q[g,\ell,Q]$ 上准确约化 grevlex 基有六项。保 $g=0$ 与 $g\ne0$ 分别处理，不能直接除 g。

若 $g=0$，原第一条 mean 的分子为
$$
(2\ell-1)(Q\ell^2-2\ell+1)=(2\ell-1)D.
$$
由 $D\ne0$，$\ell=1/2$。返回 (2.1)—(2.2)，得
$$
A_1=r=s=t=0,\qquad P_1=P_B=P_C=0,
\qquad P_0=-Q/4\ne0.
$$
原最高值和一阶 jet 因而迫 $u_1=u_B=u_C=0$，故 $U=(u_0,0,0,0)$。活跃 $K_B$ 秩二，且
$$
U=\frac{u_0}{p}K_B e_B,\qquad e_B^TK_Be_B=0.
$$
因此 $\widehat K$ 合同于 $K_B\oplus0$，秩二，违反 (1.1)。抽象方程在这里确有族；排除它用的是完整原物理秩。

若 $g\ne0$，从上述完整六项基中除去各项的 g 幂是合法必要操作。所得理想的准确约化 lex 基为
$$
g-\frac{Q^2}{5}+\frac{3Q}{20},\qquad
\ell+\frac{7Q^2}{5}-\frac{61Q}{20}-\frac12,
\qquad \frac{Q(Q-2)(4Q-3)}4.
\tag{4.2}
$$
$Q=0$ 已禁止；$Q=2$ 使 $\ell=1$，违反 $P_0\ne0$；$Q=3/4$ 使 $g=0$，违反本分支。因此整个顶点 (4.1) 为空，连同整个 $\Delta_g=0$ 面被排除。

## 5. 半比例的其余原图及完整 QQ 结式

现在仍设 $\lambda=1/2$，但由 §4 已知 $2f-1\ne0$。原 jet 准确分解为
$$
C=\frac{2f-1}{4}\bigl[-2Q^2\ell^3+2Qf\ell^2-2Qg\ell
+3Q\ell^2-2Q\ell-4f\ell+4f+2\ell-2\bigr].
$$
所以可以且必须取
$$
g=\frac{-2Q^2\ell^3+2Qf\ell^2+3Q\ell^2-2Q\ell
-4f\ell+4f+2\ell-2}{2Q\ell}.
\tag{5.1}
$$
所有此处分母都已支付。

把 (5.1) 代回同一原 $M_0,M_1,M_2,M_4,M_5$，取化简分子，只反复移去与
$$
Q(Q-1)\ell(\ell-1)D(2f-1)
$$
的 gcd，得五个多项式 $B_0,B_1,B_2,B_4,B_5$。前三者对 f 二次，后两者三次。例如第一条分子可取
$$
-4Q^2\ell^3+10Q\ell^2-5Q\ell+16f^2\ell-16f^2
-36f\ell+36f+14\ell-14.
$$
计算四个完整结果式 $\operatorname{Res}_f(B_0,B_j)$，$j=1,2,4,5$，仍只除已非零权重因子。其 $(\ell,Q)$ 次数依次为
$$
(12,8),\quad(12,6),\quad(18,11),\quad(19,12).
$$
将第一个分别与其余三个对 $\ell$ 作完整结果式，$Q$ 次数依次为 $92,162,170$，准确 QQ gcd 除非零常数外为
$$
\boxed{Q^{54}(Q-1)^8(4Q-5).}
\tag{5.2}
$$
这里保留全部首项下降的额外候选，没有以投影曲线的二元 gcd 丢弃孤立交点。

唯一尚未禁止的值为 $Q=5/4$。将它直接代回全部五个原 $B_i$，在 $\mathbb Q[f,\ell]$ 中的准确约化 lex 基为
$$
\boxed{f-\frac{5\ell}{16}-\frac12,\quad \ell^2.}
\tag{5.3}
$$
它迫 $\ell=0$，与 §3 的完整原排除矛盾。因此半比例的其余图也空。

## 6. 执行身份与剩余接口

[自含原式 QQ 源](../notes/2026-11-26-unit211-nonzero-isolated-mean-unit-base-mean-half-ratio-exclusion-347c.py)重新构造原 $E,P,N$、全部一阶 jet 和实际 $N_0=\lambda P_0$ 图；检查两个 jet 除数身份、$\ell=0$ 的原余式、顶点的两个 g 分支、完整物理 Gram 参数恢复，以及 $92/162/170$ 次结式和最后的原理想基。全部数组仅在内存中生成。源码 SHA、实际时间、峰值内存及 exit 状态见[执行回执](../notes/2026-11-26-unit211-nonzero-isolated-mean-unit-base-mean-half-ratio-exclusion-execution-347c.json)。

本稿证明 $u=1,m\ne0,P_0\ne0$ 时，$\ell\lambda(2\lambda-1)\Delta_g\ne0$；因此余下原 jet 可以合法解 g。其余比例和一般 $u\ne1$ 均继续原方程，不由本稿推断全分支为空，亦不推断 ISP 已完成。
