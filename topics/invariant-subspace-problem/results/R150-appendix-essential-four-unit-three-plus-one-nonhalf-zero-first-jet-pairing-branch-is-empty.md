# R150 附录：单位 3+1 非半权支路在一阶跨点配对为零时为空

日期：2026-11-20 UTC。AI-assisted GPT-6 Astra Pro；Astra-ISP-b2a9acde-20261120 / r150_structure，根会话独立核原方程和全部特殊返回。

## 1. 精确范围与原方程

本附录接续外均值 essential-four 的原长度五 Frobenius 支撑约化。
在 rank $H=4$ 且唯一零点是独立约化点的情形，
考虑活跃单位补空间的分拆 $3+1$。
已登记结论排除了 $p=0$、半权 $a=b=1/2$ 及非半权的一阶 mean 系数 $\alpha=0$。

以下完整排除余下的 $q=0$ 支路。因此本附录的初始假设准确为
$$
 p=1,\qquad a+b=1,\qquad b\ne0,1/2,\qquad \alpha\ne0,\qquad q=0.
                                                               \tag{1.1}
$$
这里 $p\ne0$ 后把全部 Gram 配对同时除以 $p$；
$q=0$ 不受此归一化影响，仍指原三重点的一阶 jet 与活跃单点的配对为零。

在原物理 jets 的允许局部参数规范下，
$$
 \mathcal B=\mathbb C[\epsilon]/(\epsilon^3)\oplus\mathbb C,\qquad
 \tau(z)=a z_0+z_2+b z_3,\qquad 1=(1,0,0,1),
$$
$$
 K_{\mathcal B}=
 \begin{pmatrix}
 0&0&A&1\\
 0&-2A&B&q\\
 A&B&C&r\\
 1&q&r&0
 \end{pmatrix}.                                               \tag{1.2}
$$
设
$$
 (D_Kz)_i=\tau\!\left((K_{\mathcal B})_{i,\bullet}z\right),\quad
 d=D_K1,\quad \phi=\tau(d)/2.
$$
乘法始终是 $\mathcal B$ 的实际代数乘法。
原最高阶张量及二次梯度为
$$
 T_3=P+R^3,\qquad
 P(z)=\tfrac12\tau(z-\tau(z)1)^3,\qquad N=N_{\mathcal B}+mR^2,
$$
$$
 N_{\mathcal B}(z)=
 \tfrac12\tau((d-\phi)z^2)-(\tau z)\tau(dz)
 +\phi(\tau z)^2+\tfrac14\tau(zD_Kz).                           \tag{1.3}
$$
原 mean 的活跃部分是
$$
 E=e-2D_Kd-2d^2+4\phi d=0,                                    \tag{1.4}
$$
其中若 $k_i$ 是 (1.2) 的第 $i$ 行、视为列向量，则
$$
 e=\big(\tau(k_0^2),\,2\tau(k_0k_1),\,
        2\tau(k_0k_2)+\tau(k_1^2),\,\tau(k_3^2)\big).
$$
这保留了原最高阶、原 $N$、原 mean 的必要方程；没有将有限呈示视为自由代数。

令
$$
 x=A+b,\qquad \delta=1-2b,\qquad
 \kappa=2(\phi-x)/b.
$$
原常数 mean 给出无额外除法的参数化
$$
 A=x-b,\quad r=x(1+\kappa)-\delta/2,\quad
 C=b\{\delta+\kappa(1-2x)\},\quad \phi=x+b\kappa/2.              \tag{1.5}
$$
原一次 mean 是
$$
 2\{\alpha(B+bq)+b(1/2-\kappa x)q\}=0,\qquad
 \alpha=x+b(\kappa-2).
$$
由 (1.1) 即得 $B=0$。因此以后都使用 (1.2) 中 $B=q=0$ 的原矩阵。

## 2. 两个不含除法的原梯度相容式

令
$$
 P(k_0+t k_1+t^2k_2)=p_0+p_1t+p_2t^2+O(t^3),
$$
$$
 N_{\mathcal B}(k_0+t k_1+t^2k_2)=n_0+n_1t+n_2t^2+O(t^3),
$$
并令
$$
 p_s=P(k_3),\qquad n_s=N_{\mathcal B}(k_3).
$$
这里行、列相同是因为 $K_{\mathcal B}$ 对称。

把原孤立零点的交叉配对写成
$u_0+u_1t+u_2t^2$，原最高阶和 $N$ 给出
$$
 p_0=-u_0^3,\quad p_1=-3u_0^2u_1,\quad
 p_2=-3u_0^2u_2-3u_0u_1^2,
$$
$$
 n_0=-mu_0^2,\quad n_1=-2mu_0u_1,\quad
 n_2=-m(2u_0u_2+u_1^2).
$$
因而恒有
$$
 6p_0n_2+p_1n_1-4n_0p_2=0.
$$
在当前 $B=q=0$ 矩阵上，直接由 (1.3) 有 $p_1=n_1=0$，所以
$$
                  c_1:=6p_0n_2-4n_0p_2=0.                    \tag{2.1}
$$
在活跃单点，若交叉配对为 $z$，则
$p_s=-z^3,n_s=-mz^2$。因此另有
$$
                  \chi:=n_0^3p_s^2-n_s^3p_0^2=0.             \tag{2.2}
$$
两式均没有除以 $m,u_0,z,p_0,n_0$ 或其任何组合，所有零值候选都保留。

## 3. 原 mean 的完整分解及其分母零边界

记
$$
 D_b=2-\kappa+2x\kappa(\kappa+2),\qquad
 N_b=x+\tfrac12+2x^2\kappa(1+\kappa).
$$
剩余两个原 mean 精确为
$$
 E_s=bD_b-N_b=0,\qquad E_2=R_2=0,                              \tag{3.1}
$$
$$
\begin{split}
 R_2={}&2x^2-7bx+6b^2-\tfrac12b
       +2bx^2\kappa+b^2\kappa-4b^2x\kappa\\
      &-2bx^2\kappa^2+2b^2\kappa^2-2b^2x\kappa^2.
\end{split}                                                   \tag{3.2}
$$

先处理 $D_b=0$，不能直接在 (3.1) 中除以它。
此时 $N_b=0$，而 $\kappa=0,-2$ 分别给 $D_b=2,4$，不可能。
置 $u=2x\kappa$。由 $D_b=0$ 得
$$
 u=\frac{\kappa-2}{\kappa+2}.
$$
代入 $N_b$ 得
$$
 N_b=\frac{\kappa^2+\kappa+2}{(\kappa+2)^2}.
$$
故 $\kappa^2+\kappa+2=0$，进而 $u=\kappa,x=1/2$。
在此关系下
$$
 R_2=(2b-1)\{(2-\kappa)b-\tfrac12\}.
$$
因为 $b\ne1/2$，必有 $b=1/[2(2-\kappa)]$，
从而 $\alpha=1/2+b(\kappa-2)=0$，与 (1.1) 矛盾。
所以从此以后 $D_b\ne0$。

代 $b=N_b/D_b$ 入 (3.2)，原源直接给出
$$
 D_b^2R_2=
 -\tfrac12(2x-1)(u^2+1)Q(u,\kappa),\qquad u=2x\kappa,          \tag{3.3}
$$
$$
 Q(u,\kappa)=
 (\kappa+1)(\kappa+2)u^2+2(\kappa+2)u+\kappa^2+\kappa+2.
                                                               \tag{3.4}
$$
若 $x=1/2$，则 $N_b=D_b/2$，迫 $b=1/2$，已排除。
若 $\kappa=0$，则 $u=0,Q=2$，(3.3) 仍迫 $x=1/2$。
因此 $\kappa(2x-1)\ne0$，余下的全部 mean 候选分成
$$
                u^2+1=0\quad\text{或}\quad Q(u,\kappa)=0.      \tag{3.5}
$$
两支可以相交；以下分别排除，不要求互不相交。

## 4. 二次分支 $Q=0$ 为空

令 $D=(\kappa+2)u+2-\kappa=D_b$，并记
$S=(\kappa+1)u^2+u+\kappa=2\kappa N_b$。
直接恒等式
$$
                       (\kappa+2)S+D=Q
$$
表明在 $Q=0$ 上
$$
 b=-\frac1{2\kappa(\kappa+2)},\qquad x=\frac{u}{2\kappa}.      \tag{4.1}
$$
$\kappa=-2$ 使 $Q=4$，不可能。
$\kappa=-1$ 则迫 $u=-1,b=1/2$，也已排除。
因此 $\kappa(\kappa+1)(\kappa+2)\ne0$。

在这个合法范围内写
$$
 u^2=L u+M,\qquad
 L=-\frac2{\kappa+1},\qquad
 M=-\frac{\kappa^2+\kappa+2}{(\kappa+1)(\kappa+2)}.             \tag{4.2}
$$
任一原式按 (4.2) 约为 $A(\kappa)+C(\kappa)u$ 后，定义
$$
 \mathcal N(A+Cu)=A^2+LAC-MC^2.                              \tag{4.3}
$$
若原式在一个候选点为零，其 (4.3) 也为零。
这只使用与另一线性因子相乘的恒等式，
不要求二次关系不可约或判别式非零。

按 (4.1)、(4.2) 从原 (1.3)、(2.1)、(2.2) 重建范数，有
$$
 \mathcal N(c_1)=
 \frac{9(\kappa+1)H_{10}(\kappa)}
      {256\kappa^{12}(\kappa+2)^9},                          \tag{4.4}
$$
$$
\begin{split}
 H_{10}(\kappa)={}&
 \kappa^{10}+11\kappa^9+49\kappa^8+99\kappa^7
 +125\kappa^6+175\kappa^5\\
 &+226\kappa^4+152\kappa^3-32\kappa^2-48\kappa+32.
\end{split}
$$
令 $\operatorname{num}$ 指先在 $\mathbb Q(\kappa)$ 约分，再取分子。
精确一元计算给出
$$
 \gcd_{\rm monic}\bigl(\operatorname{num}\mathcal N(c_1),
                      \operatorname{num}\mathcal N(\chi)\bigr)
                       =\kappa+1.                           \tag{4.5}
$$
配套源从 (1.3) 构造 $\chi$，在二次关系中约减后求范数，
最后直接在 $\mathbb Q[\kappa]$ 求 (4.5)；
不保存可重算的高次展开表或 Euclidean 输出表。
原有理式所有分母仅涉及
已非零的 $\kappa,\kappa+1,\kappa+2$。

由 (2.1)、(2.2)，两分子须同时为零，(4.5) 迫 $\kappa=-1$，
与本节的合法范围矛盾。整个 $Q=0$ 分支排除。

## 5. 二次分支 $u^2+1=0$ 为空，包括两个例外返回

在此分支，$S=u-1$，所以
$$
 b=\frac{u-1}{2\kappa D},\qquad x=\frac{u}{2\kappa},\qquad
 D=(\kappa+2)u+2-\kappa\ne0.                                 \tag{5.1}
$$

先处理 $\kappa^2+4=0$。
因 $u^2+1=0$，有 $\kappa=\pm2u$。
若 $\kappa=2u$，则 $D=0$，不在当前范围。
若 $\kappa=-2u$，则
$$
 D=4(u+1),\qquad b=-1/16,\qquad x=-1/4.
$$
回到原 (2.1)，模 $\kappa^2+4$ 的精确余式为
$$
                         c_1=-\frac{243(\kappa+4)}{65536}.  \tag{5.2}
$$
它与 $\kappa^2+4$ 无公共零点，故这个边界也为空。

现在 $\kappa(\kappa^2+4)\ne0$。
在 $u^2+1=0$ 上的恒等式
$$
 (u-1)(\kappa^2+4)=(\kappa+2u)D
$$
允许将 (5.1) 改写为
$$
 b=\frac{\kappa+2u}{2\kappa(\kappa^2+4)},\qquad
 x=\frac{u}{2\kappa}.                                       \tag{5.3}
$$
对 $A+Cu$ 取范数 $A^2+C^2$。
同一原源给出
$$
 \mathcal N(c_1)=
 \frac{45(\kappa^2+1)^4(5\kappa^2+8\kappa+4)}
      {128\kappa^{12}(\kappa^2+4)^4},                        \tag{5.4}
$$
$$
 \gcd_{\rm monic}\bigl(\operatorname{num}\mathcal N(c_1),
                      \operatorname{num}\mathcal N(\chi)\bigr)
                        =(\kappa^2+1)^4.                    \tag{5.5}
$$
所有分母只含本节已排除的 $\kappa=0,\kappa^2+4=0$。
故原临界候选必有 $\kappa^2+1=0$。

此时 $u=\pm\kappa$，必须回到原方程，不能把范数必要条件当充分条件。
若 $u=\kappa$，(5.3) 给 $x=b=1/2$，是已排除的半权。
若 $u=-\kappa$，则
$$
                        x=-1/2,\qquad b=-1/6.
$$
代入原 (2.1)，模 $\kappa^2+1$ 的精确余式为
$$
                           c_1=-\frac{3\kappa+11}{27}.       \tag{5.6}
$$
它与 $\kappa^2+1$ 无公共零点，所以最后的候选也排除。
整个 $u^2+1=0$ 分支为空。

## 6. 可复核结论与剩余范围

配套短源只使用原 $\mathcal B,\tau,K_{\mathcal B},P,N_{\mathcal B},E$，
精确重建 (3.1)–(3.4)、两个分母零边界、(4.4)、(5.4)、
两个 QQ 一元 gcd 及 (5.2)、(5.6) 的原式返回。
它不使用一般多元 Gröbner、有限域正证提升或未声明的非零除数。
重算所需全部输入均在正文与源中；不持久化可重算输出表。

因此，单位 $3+1$ 加孤立零点的外均值 essential-four 原临界候选，
在已付的 $p=0$、半权、$\alpha=0$ 排除之后，还必须满足
$$
                        p\,q\,\alpha\ne0,\qquad b\ne1/2.
$$
本附录完整关闭 $q=0,\alpha\ne0$ 的剩余支路。
它没有声称关闭 $p q\alpha\ne0$ 的真正一般支、
其他活跃补空间分拆、rank $H=5$，或普通 Hilbert ISP 主问题。


## 7. 实际成功核验与精确算法

[冻结原QQ验证源](../notes/2026-11-20-essential-four-unit-three-plus-one-q-zero-verify.py)在[run44737710336](https://github.com/Rogerhu12/math-research-public/actions/runs/44737710336)、job136293190180的独立标签 `unit31_q_zero` 成功，exit0，源内1.484秒、外层1.9757839629999694秒。触发提交 `2b27f6da9af4b7e80ec9e94d75d10b504e34c7aa`，Python3.12.14/SymPy1.13.3/mpmath1.3.0；180秒上限保持不变。

五个原低阶多项式 $p_0,n_0,p_s,n_s,c_1$ 逐单项式在二元商代数 $\mathbb Q(\kappa)[u]/(u^2-Lu-M)$ 中求值。每次乘法即时按 $(a,c)(d,e)=(ad+Mce,ae+cd+Lce)$ 约减，再从原式计算 $\chi$、范数和原生一元QQ gcd。这样避免先在一般有理式中膨胀后才约减；数学输入和两个必要范数均保持原样。

源SHA-256 `0dfb482af62883fcf5e7c79af96d2b1a5a2a726a973320c5ff93be86d94fb397`；完整独立stdout SHA-256 `f10fede6807be1240f646b2ccf5035df5f4d546f8893e385fd2ef2149add90b1`。原mean分解、两个norm/gcd与全部例外返回逐项通过。[执行身份](../notes/2026-11-20-exact-source-run44737710336-b2a9.json)仅保时间、参数和SHA。旧run44736004677的180秒展开超时单独保留，不将未完成段冒称证据；同一新job中其他源的特殊纤维次数断言失败也不改变本独立标签的完整成功。
