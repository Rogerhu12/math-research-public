# R598：真实变化导子负根号族的统一导数均值与高维秩商

日期：2026-11-14。状态：**已证明下述充分区域；绝对目标仍 OPEN。**

恢复说明：这是环境重置后按已发送并经根代理逐式审核的论证重建的正文。原 `r598_proof_checkpoint_v4` 字节已丢失；本稿必须使用重新计算的 SHA256，不能声称原哈希复原。任意水平的秩接口完整见同目录 `general-level-Heegner-rank-interface.md`，本文也列出实际使用的每一步。

## 1. 实际族、范围和结论

沿用已发布 R317、R575 及本次完整恢复的 R587 实际偶分支。写

\[
 r=1-a^3=db^3,\quad d>0\text{ 立方自由},\quad
 p>37,\quad p\equiv2,5\pmod9,
\]
\[
 2\nmid d,\quad3\nmid d,\quad d\equiv\pm1\pmod9,
 \qquad D=\prod_{\substack{q\ge5, q\ne p\\q\mid d}}q,
 \quad s(D)=\#\{q\mid D:q\equiv2\pmod3\}.
\tag{598.1}
\]

这里 \(D\) 只记录额外坏素数的无平方支撑；\(s(D)\) 只数其中的惰性素数，不数所有额外素数。使用的实际权二模形式是

\[
 g_{\theta,d}=\operatorname{AI}_{K/\mathbb Q}
       (\Psi\theta\kappa_4\kappa_d^{-1}),\qquad
 K=\mathbb Q(\zeta_3).
\tag{598.2}
\]

其水平和根号已在 R587 按全部局部因素固定为

\[
 N_d=108p^2D^2,\qquad
 \epsilon(g_{\theta,d})=(-1)^{s(D)+1}.
\tag{598.3}
\]

本篇处理 \(s(D)\) 为偶数，因此是负根号族。它不是旧的反向 \(\kappa_4^{-1}\) 家族，也不以辅助的高权 \(\xi_1,\xi_3\) 中心值代替实际 (598.2)。

令

\[
 C=\mathbb F_{p^2}^{\times}/\mathbb F_p^{\times},\quad |C|=p+1,
 \quad\Theta_p=\{\theta:\theta(\zeta_3)=\zeta_3^{-1},\ \theta(s)=-1\},
\tag{598.4}
\]

其中 \(s\) 是 \(C\) 的唯一二阶元。则 \(h=|\Theta_p|=(p+1)/6\)。

**定理 598.1。** 若 \(s(D)\) 偶且 \(p\ge1000D\)，则

\[
 \frac1h\sum_{\theta\in\Theta_p}L'(g_{\theta,d},1)>\frac95.
\tag{598.5}
\]

同时，对每个 \(\theta\in\Theta_p\)，有无须均值的统一界

\[
 |L'(g_{\theta,d},1)|\le4\sqrt{3\sqrt3\,pD}.
\tag{598.6}
\]

因此至少有一个 **实际维数至少二** 的 \(\mathbb Q\)-单因子 \(A_{\theta,d}\)，满足

\[
 \operatorname{rank}A_{\theta,d}(\mathbb Q)
 =\dim A_{\theta,d},
 \qquad
 \log_p:A_{\theta,d}(\mathbb Q)\otimes\mathbb Q_p
       \xrightarrow{\sim}\operatorname{Lie}(A_{\theta,d})(\mathbb Q_p).
\tag{598.7}
\]

本篇不保证这个 \(\theta\) 是指定的 \(\theta_{-1}\)，也不声称 (598.7) 使有理点在商中为零。它给实际二次高度法的全局秩输入。

## 2. 角色规范及精确 AFE

固定 \(\chi=\chi_{-3}\)，并记

\[
 c=L(\chi,1)=\frac{\pi}{3\sqrt3},\quad
 t=\frac{c}{pD}=\frac{2\pi}{\sqrt{N_d}},\quad
 E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du.
\tag{598.8}
\]

\(K\) 的类数为一。对与导子互素的主理想，在固定复嵌入下的真实 Hecke 角色写为

\[
 (\Psi\theta\kappa_4\kappa_d^{-1})((\alpha))
 =\epsilon_3(\alpha)\theta(\alpha\bmod p)\xi_d((\alpha))\alpha.
\tag{598.9}
\]

这里末项是 \(\alpha\)，不是 \(\overline\alpha\)；\(\xi_d=\kappa_4\kappa_d^{-1}\) 是反圆分三次角色。它在有理主理想 \((n)\) 上为一：复共轭固定该理想，反圆分性又使其值取逆，三次单位根中只有一满足这两件事。

对负根号的权二形式，完成的 Mellin 公式及 \(s\leftrightarrow2-s\) 给精确导数 AFE

\[
 L'(g_{\theta,d},1)
 =2\sum_{n\ge1}\frac{a_n(g_{\theta,d})}{n}E_1(tn).
\tag{598.10}
\]

可直接由把 Mellin 积分在 \(1/\sqrt{N_d}\) 分开并用负 Fricke 符号获得；在一侧作积分交换，核是 \(E_1\)。亦见 Derickx–Le Fourn 的 Lemma 15 中同一权二导数公式，水平无需为奇数：

<https://link.springer.com/article/10.1007/s00208-020-02112-3>

## 3. 正交平均的两条直线

把 (598.10) 写成 \(\mathbb Z[\zeta_3]\) 的格点和，除去六个单位的重数。对 (598.4) 完整的 \(\Theta_p\) 取平均，正交性只留下 \(C\) 中的六阶子群。六个方向经单位旋转准确合并为以下两类：

\[
 L_R:\quad \alpha=a+b\zeta_3,\quad b\equiv0\pmod p,
\]
\[
 L_I:\quad \alpha=a+b\zeta_3,\quad2a-b\equiv0\pmod p.
\tag{598.11}
\]

有理方向的相位是正，纯虚方向的相位是负。此处用的是 (598.4) 的两个真实限制；不能换成对所有 tame 角色取平均。\(L_R\) 的精确有理射线 \(b=0\) 给

\[
 2G_{2pD}(t),\qquad
 G_M(t)=\sum_{\substack{n\ge1\\(n,M)=1}}
               \frac{\chi(n)}nE_1(tn^2).
\tag{598.12}
\]

\(L_I\) 的精确纯虚射线 \(2a-b=0\) 被三处导子删掉，因为相应 \(\alpha\) 被 \(\sqrt{-3}\) 整除。故它不产生抵消 (598.12) 的第二个主项。

其余格点的范数分别可写

\[
 \operatorname N(a+pb\zeta_3)
 =(a-pb/2)^2+3p^2b^2/4\quad(b\ne0),
\]
\[
 \operatorname N(\alpha)=p^2k^2/4+3b^2/4,
 \quad k\ne0,\quad b\equiv k\pmod2.
\tag{598.13}
\]

因此偏离两个精确射线的项都具有范数至少 \(p^2/4\)。这一范数下界只对完整 \(\Theta_p\) 的两直线成立；后续本原 Möbius 筛增加的方向不能不经证明沿用它。

记

\[
 A=\frac{cp}{4D},\qquad
 \mathcal Q(x)=\frac{e^{-x}}{1-e^{-3x}}.
\tag{598.14}
\]

使用 \(E_1(x)\le e^{-x}/x\)、\(\sum_{m\in\mathbb Z}e^{-u(m+v)^2}\le1+\sqrt{\pi/u}\)，以及 \(j^2\ge1+3(j-1)\)，对 (598.13) 两个纵向求和得

\[
 \left|\frac1h\sum_\theta L'(g_{\theta,d},1)-2G_{2pD}(t)\right|
 \le E_{\rm off},
\tag{598.15}
\]
\[
 E_{\rm off}=
 \frac4p\left[
 \left(\frac1{\sqrt3}+3^{1/4}\sqrt{pD}\right)
       \frac{\mathcal Q(3A)}{3A}
 +\left(1+3^{1/4}\sqrt{pD}\right)
       \frac{\mathcal Q(A)}A\right].
\tag{598.16}
\]

第一括号的 \(3^{1/4}\) 来自 \((1/\sqrt3)\sqrt{\pi/t}\)；第二括号来自步长二的 \(b\)-格点和 \(\sqrt{\pi/(3t)}\)。因此没有漏掉 \(\sqrt3\) 的尺度。

## 4. Poisson 恒等式和射线主项

定义

\[
 F(t)=\sum_{n\ge1}\frac{\chi(n)}n e^{-tn^2},\qquad
 H(t)=\sum_{n\ge1}n\chi(n)e^{-tn^2}.
\]

三模奇角色的 Poisson 公式给

\[
 H(t)=\left(\frac\pi{3t}\right)^{3/2}
       H\!\left(\frac{\pi^2}{9t}\right).
\tag{598.17}
\]

由 \(F'(t)=-H(t)\)、\(F(0)=c\)，积分得到精确式

\[
 F(t)=c-\frac\pi{\sqrt3}
       \sum_{n\ge1}\chi(n)
       \operatorname{erfc}\!\left(\frac{\pi n}{3\sqrt t}\right).
\tag{598.18}
\]

用 \(\operatorname{erfc}(x)\le e^{-x^2}/(\sqrt\pi x)\)，可得

\[
 |F(t)-c|\le\sqrt{\frac{3t}{\pi}}
       \mathcal Q\!\left(\frac{\pi^2}{9t}\right).
\tag{598.19}
\]

记 \(G=G_1\)。由 \(G'(t)=-F(t)/t\)，以及 Mellin 表达中 \(\Gamma(s)L(1+2s,\chi)/s\) 在零点的双极部分，得到

\[
 G(t)=c\log(1/t)+2L'(\chi,1)-\gamma c+R(t),
\]
\[
 |R(t)|\le2\sqrt{\frac{3t}{\pi}}
       \mathcal Q\!\left(\frac{\pi^2}{9t}\right).
\tag{598.20}
\]

该余项也可直接写作 \(\int_0^t(c-F(u))\,du/u\)，结合 (598.19) 获得；主项常数由上述 Mellin 留数固定。

取 \(M=2D\)。有限包含排除给

\[
 G_M(t)=\sum_{e\mid M}\frac{\mu(e)\chi(e)}eG(te^2)
       =cP_M B_M+R_M,
\tag{598.21}
\]

其中

\[
 P_M=\prod_{q\mid M}\left(1-\frac{\chi(q)}q\right),
\]
\[
 B_M=\log(1/t)-\gamma+\frac{2L'(\chi,1)}c
             +2\sum_{q\mid M}\frac{\chi(q)\log q}{q-\chi(q)}.
\tag{598.22}
\]

因为 \(e\le2D\)、\(\tau(2D)\le2D\)，(598.20) 给

\[
 |R_M|\le4\,3^{-1/4}\sqrt{\frac Dp}\,\mathcal Q(3A).
\tag{598.23}
\]

表示素数 \(p\) 处 \(\chi(p)=-1\)，所以

\[
 G_{2pD}(t)=G_M(t)+\frac1pG_M(tp^2).
\tag{598.24}
\]

后一项不被不加控制地当正数；其对完整主项的误差满足

\[
 E_p:=\frac2p|G_M(tp^2)|
 \le\frac2p\frac{\mathcal Q(4A)}{4A}.
\tag{598.25}
\]

## 5. 保留 Euler 因子的统一下界

额外分裂素数很多时 \(P_M\) 可变小，故不能把 \(D=1\) 的主项常数直接用于变化 \(D\)。本节同时控制该损失和其导数。

首先 \(L'(\chi,1)>0\)。将条件收敛级数按相邻非零项分组，初项

\[
 \frac{\log2}2-\frac{\log4}4=0,
\]

其后的每一项均形如

\[
 \frac{\log(3j+2)}{3j+2}-\frac{\log(3j+4)}{3j+4}>0
 \quad(j\ge1),
\]

因为 \(\log x/x\) 在 \(x>e\) 递减。

其次

\[
 P_M\ge\frac32\prod_{q\mid D}(1-1/q)
 \ge\frac{3}{2\zeta(2)(1+\log D)}.
\tag{598.26}
\]

最后一个不等式来自

\[
 \prod_{q\mid D}(1-1/q)^{-1}
 =\prod_{q\mid D}\frac{1+1/q}{1-1/q^2}
 \le\zeta(2)\sum_{e\mid D}\frac1e
 \le\zeta(2)(1+\log D).
\]

对 (598.22) 的 Euler 导数，分裂素数的项为正；惰性素数 \(q\ge5\) 的负项满足 \(2/(q+1)\le1/3\)。因此

\[
 2\sum_{q\mid M}\frac{\chi(q)\log q}{q-\chi(q)}
 \ge-\frac23\log2-\frac13\log D.
\tag{598.27}
\]

若 \(p\ge1000D\)，用 \(c<1\)、\(\gamma<1\)、\(\log2<1\)、\(\log1000>4\)，便有

\[
 B_M>\frac53(1+\log D).
\tag{598.28}
\]

于是

\[
 2cP_MB_M>\frac{10}{\pi\sqrt3}>\frac{20}{11}.
\tag{598.29}
\]

第二个不等式可用 \(\pi<22/7\)、\(\sqrt3<7/4\) 精确核实。

此时 \(A\ge125\)。从 (598.16)、(598.23)、(598.25) 可统一得到

\[
 E_{\rm off}+2|R_M|+E_p<\frac1{1000}.
\tag{598.30}
\]

例如，\(\mathcal Q(x)<2e^{-x}\) 在这里成立，\(p\ge1000\)、\(\sqrt{p/D}>30\) 给

\[
 E_{\rm off}<\frac{2e^{-125}}{125},\qquad
 2|R_M|<\frac{16}{30}e^{-375},\qquad
 E_p<\frac4{1000}\frac{e^{-500}}{500}.
\]

只用 \(e^x>x^3/6\) 已使三个上界之和远小于 (598.30)，无需浮点近似作为证明。由 (598.15)、(598.21)、(598.24)、(598.29) 得

\[
 \frac1h\sum_\theta L'(g_{\theta,d},1)
 >\frac{20}{11}-\frac1{1000}>\frac95,
\]

即 (598.5)。

## 6. 单项上界以及排除全部非消失都落在维一因子

设 \(a_K(n)\) 为 \(K\) 中范数为 \(n\) 的整理想数，\(A_K(X)=\sum_{n\le X}a_K(n)\)。由于类数一，每个理想对应六个生成元。对 \(\alpha=a+b\zeta_3\)，定义六角壳半径

\[
 \rho=\max(|a|,|b|,|a-b|).
\]

有 \(\operatorname N(\alpha)\ge3\rho^2/4\)，半径 \(R\) 的六角形共有 \(1+3R(R+1)\) 个格点。因此对 \(X\ge3\)，

\[
 A_K(X)\le\frac{R(R+1)}2
 \le\frac{2X}3+\sqrt{\frac X3}\le X.
\tag{598.31}
\]

当 \(1\le X<3\) 时只有范数一的单位理想，故同一界仍成立；\(X<1\) 时为零。

Hecke 角色的绝对值给 \(|a_n(g)|\le\sqrt n\,a_K(n)\)。取正递减函数 \(f(x)=x^{-1/2}E_1(tx)\)，对 Stieltjes 积分分部积分，再用 (598.31)，得

\[
 \sum_{n\ge1}a_K(n)f(n)\le\int_0^\infty f(x)\,dx
 =2\sqrt{\frac\pi t}.
\]

结合 (598.10)，就是 (598.6)。

若 \(r_\theta=\operatorname{ord}(\theta)\)，则本实际族的系数域是

\[
 F_\theta=\mathbb Q(\mu_{r_\theta})^+,
 \qquad\dim A_{\theta,d}=\frac{\varphi(r_\theta)}2.
\tag{598.32}
\]

为说明没有漏掉更小的系数域，注意 \(6\mid r_\theta\)。固定 \(K\) 的圆分 Galois 自同构固定 \(\Psi\) 和三次角色 \(\kappa_4\kappa_d^{-1}\)，只把 \(\theta\) 改为相应幂。若诱导形式不变，限制到 \(G_K\) 后，两个无穷型不同的分量不能互换，因此必固定 \(\theta\)。这个稳定子计算给 (598.32)。

维数一只可能 \(r_\theta=6\)，而 (598.4) 内至多有一个这样的角色。全族导数总和大于 \(3(p+1)/10\)，而

\[
 \frac{3p}{10}\ge3\sqrt{10}\sqrt{pD}
 >4\sqrt{3\sqrt3\,pD}
 \qquad(p\ge1000D).
\tag{598.33}
\]

所以不可能只有这个至多一个维一角色提供非零导数。至少有一个维数至少二的实际因子满足 \(L'\ne0\)。

## 7. 任意水平的秩与对数接口

对上节选出的实际 \(g_{\theta,d}\)，使用 BFH 1990 Introduction Theorem **(ii)**，对任意含水平素数的有限 \(S\)，选择虚二次辅助域 \(K_{\rm aux}\)，使所有水平素数分裂且 \(L(g_{\theta,d}\otimes\chi_{K_{\rm aux}},1)\ne0\)。若需排除任何有限个辅助域，将各域一个惰性素数加入 \(S\) 即可；此量词也严格推出无限多个选择。特别可取 \(K_{\rm aux}\ne\mathbb Q(\sqrt{-3})\)。

split-Heegner Gross–Zagier 公式使完整类迹 \(P\) 非挠。Nekovář *The Euler system method for CM points on Shimura curves* Theorem 3.2 取 \(\alpha=1\)，结合其 §3.4，CM 条件只排除由 \(K_{\rm aux}\) 产生的 CM；这里两二次域不同，故得到 \(A(K_{\rm aux})\otimes\mathbb Q=F_\theta P\)。

复共轭对完整理想类轨道与 Fricke 对合的作用相同，尖点基点差为挠。因 \(W_Ng=-\epsilon(g)g=+g\)，\(P\) 的有理倍数非挠，故 \(\operatorname{rank}A(\mathbb Q)=\dim A\)。这个理想类论证包括本篇偶水平，不误用只在奇水平表述的命题。

同一非挠 \(F_\theta\)-直线的各实分量具有正高度，给全部共轭的一阶非消失。实际 \(p\) 进对数在这个秩一 \(F_\theta\otimes\mathbb Q_p\)-模上的任何零特征分量，会由 \(p\) 进解析子群定理给一个包含有理非挠点倍数的真 \(\mathbb Q\)-阿贝尔子簇，违反 \(\mathbb Q\)-单性。因此对数是同构，得到 (598.7)。

完整基点、Fricke 符号、BFH 量词和解析子群论证见本稿开头指定的共同接口文件；其原始来源为：

- BFH 1990：<https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf>，Introduction Theorem (ii)，543–544 页。
- Cai–Shu–Tian：<https://arxiv.org/pdf/1408.1733>，Theorem 1.1 的 split-Heegner 情形。
- Nekovář：<https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf>，Theorem 3.2、§3.4。
- 理想类共轭公式的独立对照：<https://link.springer.com/article/10.1007/s00208-020-02112-3>，Appendix (49)–(50)；不将其奇水平 Prop. 8 扩用为本篇的定理。

## 8. 保留的实际缺口

本结果未覆盖 \(p<1000D\)，也未处理 \(s(D)\) 奇的正根号族。正根号中心值可另用指数核研究，但不得用本篇的导数核替代。

所选 \(\theta\) 不必本原，故尚不能直接与指定 \(\theta_{-1}\) 的局部首项拼接。R600 专门处理这个同轨道选择问题。

实际因子的秩等于维数并不消灭其有理像；相应二次高度关系仍需要同一商上的实际高度系数和局部展开。本篇也没有从局部配对匹配推出原全局模 \(p\) 同构。新增支撑约束可在后续结合，但不改写这些量词。
