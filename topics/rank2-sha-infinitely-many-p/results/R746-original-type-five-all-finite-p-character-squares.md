# R746：原两条 degree34 型五来源的全部有限 p-角色平方与真实分歧域

## 0. 状态与准确范围

本篇在 R735 的同一个普通素数、同一个 CM 嵌入、同一个有界 theta 测度上，
支付任意有限 p-层测试的完整角色展开及每个存活角色的精确 Katz 平方。
包括所有 tame 分支和任意 p-primary 深度；不要求该值非零。

本篇不将一般有限门的积分预先认作代数点的对数。
后者仍需要把本篇的同一 Katz 值与准确周期下的 ramified CM/Heegner 公式接齐。
尤其不能用“相差一个未指定 Iwasawa 单位”替代代数比例系数。
本篇也不把整个五维型五空间认作以下两条直线。

固定
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
\theta=17^{1/6},\qquad
E_k:y^2=x^3+17^k\quad(k=2,4).
\tag{1}
$$
使用 R735 的完整 Hecke 角色 $\psi_k$、
原两条来源 $D_{k,17}$、固定非零代数常数 $c_k$，
以及其规范微分 $dx/(2y)$。
普通素数 p 满足 R735 的全部已付条件；
特别 $p\nmid2\cdot3\cdot17$ 且 $p\equiv1\pmod6$。
原两个普通周期为
$$
\Omega_{p,0}=\theta\Omega_p.
\tag{2}
$$
同一个固定嵌入 $\overline{\mathbf Q}\hookrightarrow\mathbf C_p$ 始终保留。

记 $\nu_{k,17}$ 为 Amice 变换
$D_{k,17}(\Omega_p\log(1+T))$ 的原有界测度。
R735 的真正来源缩放是
$$
\nu_{k,1}=\theta^5\nu_{k,17}.
\tag{3}
$$
它不缩放测度变量 x，因此不会改变任何单位门或有限角色。

## 1. 全部有限角色、角型与完整有限测试

对任意有限连续角色
$$
\chi:\mathbf Z_p^\times\longrightarrow\overline{\mathbf Q}^{\,\times},
$$
定义原负一单位行
$$
I_{k,\chi}
=\int_{\mathbf Z_p^\times}x^{-1}\chi(x)\,d\nu_{k,17}(x).
\tag{4}
$$
这里角色可以有任意 tame 部分、任意 p-power 部分；
其最小导子可以是1，也可以是 $p^n$，$n\ge1$。

R735 的完整型五身份是
$D_{k,17}(\zeta z)=\zeta^5D_{k,17}(z)$，
其中 $\zeta\in\mu_6\subset K$，并在普通嵌入下属于 $\mathbf Z_p^\times$。
Amice 变换的单射性给
$$
[\zeta]_*\nu_{k,17}=\zeta^5\nu_{k,17}.
\tag{5}
$$
在 (4) 上测试 (5)，得到
$$
\bigl(\chi(\zeta)-1\bigr)I_{k,\chi}=0.
$$
因而
$$
\boxed{\chi|_{\mu_6}\ne1\quad\Longrightarrow\quad I_{k,\chi}=0.}
\tag{6}
$$
这只声明原积分为零；
不向这种不存活的角色套用下文固定 $c_k$ 的 Katz 身份。

任取 $\ell\ge1$ 及代数值有限测试
$\Phi:(\mathbf Z/p^\ell\mathbf Z)^\times\to\overline{\mathbf Q}$。
令
$$
\widehat\Phi(\chi)
=\frac1{\varphi(p^\ell)}
 \sum_{a\in(\mathbf Z/p^\ell\mathbf Z)^\times}
       \Phi(a)\chi(a)^{-1}.
$$
有限群角色的完整正交关系给
$$
\boxed{
\int_{\mathbf Z_p^\times}x^{-1}\Phi(x)\,d\nu_{k,17}(x)
=\sum_{\substack{\chi\bmod p^\ell\\\chi|_{\mu_6}=1}}
       \widehat\Phi(\chi)I_{k,\chi}.
}
\tag{7}
$$
没有省掉 tame 角色。等价地，原积分只读取
$6^{-1}\sum_{\zeta\in\mu_6}\Phi(\zeta x)$。

(7) 是线性恒等式；下面的单角色平方不能用来删除
$(\sum_\chi\widehat\Phi(\chi)I_{k,\chi})^2$ 中的交叉项。

## 2. 真实全局角色及点域候选

令 $\widehat\psi_k,\widehat{\bar\psi}_k$ 为 R735 同一 ordinary CM 型的 p-adic Galois avatars。
两者为 $G_K^{\mathrm{ab}}$ 上的连续单位值角色，并且
$$
\Gamma_k=\frac{\widehat\psi_k}{\widehat{\bar\psi}_k}
:G_K^{\mathrm{ab}}\longrightarrow\mathbf Z_p^\times,
\qquad
\Gamma_k^c=\Gamma_k^{-1}.
\tag{8}
$$
对任意 $\chi$ 定义
$$
\rho_{k,\chi}=\chi\circ\Gamma_k.
\tag{9}
$$
这是先在整个 Galois 群定义的实际有限角色，
不是只指定一个 p-adic 局部角色再任意补成全局角色。
其对角有理 idèle 限制为1，所以它是反循环角色。
本篇使用几何 Artin reciprocity；
在两 p-处的单位上，完整 CM 型给
$$
\rho_{k,\chi,\mathfrak p}(u)=\chi(u)^{-1},
\qquad
\rho_{k,\chi,\bar{\mathfrak p}}(u)=\chi(u).
\tag{10}
$$
采用反向 reciprocity 时两式同时取逆，不能只改一处。

现在假定 $\chi|_{\mu_6}=1$。
在每个有限 $v\nmid p$：

- 若 $v\nmid2\cdot3\cdot17$，两原 CM 角色都不分歧；
- 在2、3、17处，R735 的完整有限角色表给有限惯性像包含于 $\mu_6$。
  因此 $\Gamma_k(I_v)\subseteq\mu_6$，被 $\chi$ 消掉。

故
$$
\boxed{\rho_{k,\chi}\text{ 在所有 }v\nmid p\text{ 不分歧，尤其在 }2,3,17\text{ 不分歧。}}
\tag{11}
$$
uniformizer 上的值可以不为1；(11)不删除这些值。
不分歧只要求惯性限制为1。

若 $\chi$ 的最小导子为 $p^n$，$n\ge1$，
由 (10) 两个局部导子的指数都准确为 n，故
$$
\mathfrak f(\rho_{k,\chi})
=\mathfrak p^n\bar{\mathfrak p}^{\,n}.
\tag{12}
$$
若 $\chi=1$，则 $\rho_{k,\chi}=1$。
令
$$
H_{k,\chi}=\overline K^{\ker\rho_{k,\chi}}.
\tag{13}
$$
这是一个只可能在 p 上分歧的有限阿贝尔扩张。
特别，它同时通过“在17不分歧”和“在2与17不分歧”这两种域门。

(13)是有限角色的实际点域候选，不是已经构造出的 Heegner 点。
若后来通过同一角色的 CM twist descent 得到
$E_k(H_{k,\chi})\otimes\overline{\mathbf Q}$ 中的点，
其点坐标域确实具有上述性质。
角色值域或投影系数域可能另有分歧；
它们属于代数系数，不能与点坐标的定义域混同。

对存活 $\chi$，在原坏处乘上 (9) 不改变
$\bar\psi_k$ 的惯性角色或导子。
因此原 $2,3,17$ 的全部坏 Euler 因子仍按 R735 保留原 ramified 规范；
没有因为加入 $\chi$ 而产生 conductor cancellation。
当 $n\ge1$ 时两 p-处都分歧，不能再插入无分歧 p-Euler 因子；
原 Katz 测度在此值处的 Gauss/局部规范由同一个测度本身决定。

## 3. 每个 tame 分支上的有界解析身份

以下论证说明为什么只知道正整数权的原平方，
也能到达所有有限 p-primary 角色。
有限 torsion 点不需要在小指数盘中被整数权直接逼近。

令 $\mathscr W$ 为 $\mathbf Z_p^\times$ 的 p-adic weight space。
对任意连续角色 $\eta$ 写
$$
\mathcal M_k(\eta)
=\int_{\mathbf Z_p^\times}\eta(x)\,d\nu_{k,1}(x).
\tag{14}
$$
单位有界测度保证 $\mathcal M_k$ 在 $\mathscr W$ 的每个 tame 分支上
为有界刚性解析函数。

记 $\mathcal L^{\mathrm{prim}}_{p,34\delta}$ 为 R735 已固定的
primitive Katz 测度，复/普通周期同时按 (2) 规范。
在以下各分支上原 tame 惯性角色不变，且是非平凡的原角色，
所以使用的确是该有界测度，不引入未定义的伪测度分母。
定义
$$
\mathcal K_k(\eta)=
 \mathcal L^{\mathrm{prim}}_{p,34\delta}
       \bigl(\widehat\psi_k\cdot(\eta\circ\Gamma_k)\bigr).
\tag{15}
$$
这是把同一个 Katz 测度按 $\Gamma_k$ 推前并用
$\widehat\psi_k$ 加权得到的有界解析函数。

取任何整数 a 满足
$$
a\equiv5\pmod6.
$$
考虑 tame 限制为 $x\mapsto x^a$ 的整个 weight-space 分支。
固定任意整数 $b\equiv a\pmod{p-1}$，并令
$$
m_j=b+(p-1)p^j.
\tag{16}
$$
对充分大的 j，$m_j\ge0$ 且 $m_j\equiv5\pmod6$，
因而 R735 的全正权公式准确适用：
$$
\mathcal K_k(x^{m_j})
=c_k\Omega_{p,0}34^{-m_j}
 \left(1-\frac{\alpha_k^{m_j}}{\bar\alpha_k^{\,m_j+1}}\right)^2
 \left(\int_{\mathbf Z_p}x^{m_j}\,d\nu_{k,1}\right)^2,
\tag{17}
$$
其中 $v_p(\alpha_k)=1$，$v_p(\bar\alpha_k)=0$。

逐项取极限：

1. $m_j\to b$ p-adically，且对整个 $\mathbf Z_p^\times$，
   $x^{m_j}\to x^b$ 一致收敛。
2. 在非单位域，$|x^{m_j}|_p\le p^{-m_j}\to0$；
   有界测度因此给非单位矩趋0。
3. 原 ordinary Euler 减项的赋值为 $m_j$，
   故其平方因子趋1。这一步没有把有限层的原 Euler 因子先删掉。
4. $34^{-m_j}\to34^{-b}$；
   Katz 左端由同一个有界测度连续收敛。
   所有涉及周期的指数已经包含于原矩，未对 $\Omega_{p,0}$ 作任意指数延拓。

从而
$$
\mathcal K_k(x^b)
=c_k\Omega_{p,0}34^{-b}\mathcal M_k(x^b)^2.
\tag{18}
$$
等式对该 tame 分支的全部整数 b 成立。
取 $b_j=a+(p-1)p^j$，得到分支内部的无限零点序列，
其极限是角色 $x^a$。
两侧都是整个 open weight-disc 上的刚性解析函数，
故恒等原理给
$$
\boxed{
\mathcal K_k(\eta)
=c_k\Omega_{p,0}\,\eta(34^{-1})\,\mathcal M_k(\eta)^2
\quad\text{在整个分支上成立。}
}
\tag{19}
$$

允许的 tame 分支恰是 $a\equiv5\pmod6$ 的 $(p-1)/6$ 个分支。
有限 p-primary 角色在这些完整 open discs 内；
它们通常不在 $\{x^b:b\in a+(p-1)\mathbf Z_p\}$ 的连续像内。
本篇使用的是 (19) 的解析恒等延拓，不是错误的 torsion 稠密性。

## 4. 所有存活有限角色的精确原平方

若 $\chi|_{\mu_6}=1$，则
$$
\eta_\chi(x)=x^{-1}\chi(x)
$$
恰位于上一节某个合法 tame 分支。
由 (8)、(9)：
$$
\widehat\psi_k\cdot(\eta_\chi\circ\Gamma_k)
=\widehat{\bar\psi}_k\,\rho_{k,\chi},
\qquad
\eta_\chi(34^{-1})=34\,\chi(34)^{-1}.
$$
把它代入 (19)，再用 (2)、(3)，得到本篇主式：
$$
\boxed{
\mathcal L^{\mathrm{prim}}_{p,34\delta}
      (\widehat{\bar\psi}_k\,\rho_{k,\chi})
=34c_k\theta^{11}\Omega_p\,
     \chi(34)^{-1}I_{k,\chi}^{\,2},
\qquad k=2,4.
}
\tag{20}
$$

(20)的全部非零标量都是原来的准确标量或显示的有限角色值：
$c_k\in\overline{\mathbf Q}^{\,\times}$ 固定，
$\theta$ 是 (1) 的固定根，
$\chi(34)^{-1}$ 是代数根单位，
$\Omega_p$ 是原普通周期。
没有未指定的 Iwasawa 单位或随字符改变的解析比例。

(20)也包括 $I_{k,\chi}=0$ 的情形；
其左端在该情形准确为0。
对 $\chi=1$，它逐字恢复 R735 的原负一身份。
对 $n\ge1$，它仍是同一个 Katz 函数在真正 p-ramified 点上的值，
不是用无分歧插值公式重新定义该值。

## 5. 与点对数空间的严格接口

本篇已付的是 (6)、(7)、(11)–(13)、(20)。
为说明后续所需比较，假定对某一个存活 $\chi$ 已经另行支付
同一 Katz 值的准确 ramified CM 点身份
$$
\mathcal L^{\mathrm{prim}}_{p,34\delta}
      (\widehat{\bar\psi}_k\,\rho_{k,\chi})
=\varepsilon_{k,\chi}\,
 \Omega_{p,E_k}^{-1}
 \log_{\omega_{E_k}}(P_{k,\chi})^2,
\quad
\varepsilon_{k,\chi}\in\overline{\mathbf Q}^{\,\times},
\tag{21}
$$
其中实际点或有限代数点组合属于
$E_k(H_{k,\chi})\otimes\overline{\mathbf Q}$，
并且
$\Omega_{p,E_k}=\theta^{-k}\Omega_{p,0}$。
那么原代数同构 $\phi_k:E_k\to E_1$ 满足
$\phi_k^*\omega_1=\theta^k\omega_{E_k}$，
故 (20)、(21) 立即给
$$
\boxed{
\Omega_p I_{k,\chi}
=A_{k,\chi}\log_{\omega_1}(\phi_kP_{k,\chi}),\qquad
A_{k,\chi}^{\,2}
=\frac{\varepsilon_{k,\chi}\chi(34)\theta^{-k-12}}{34c_k}
\in\overline{\mathbf Q}^{\,\times}.
}
\tag{22}
$$
若两侧为零，同样成立。
在仅证明“属于代数点 logarithm 的 $\overline{\mathbf Q}$-span”时，
按实际值选择平方根即可，其平方代数保证该根仍代数；
不需要为所有 $\chi$ 预选相容的符号。
若要计算真实投影系数或相消，则仍需要线性等变的完整映射。

(21)在本篇是明确列出的后续前提，不是本篇结论。
Liu–Zhang–Zhang 的 Proposition 4.3.6 确实给任意有限 p-导子的
universal torus period 等于实际有限 CM 点和的对数，
但仍须识别 (20) 的原 theta 平方与该同一 period、
保完整 local factors 和周期。
仅得到两种未配对对数的乘积，或得到任意 p-adic 单位比例，
均不足以直接宣布 (21)。

对一般伴随已积分系数，本篇也没有把它们自动认作代数数。
只有当实际来源及周期齐次性已证明 (7) 的系数为代数数时，
才能将各单角色的点空间结论线性合并。
全有限门/正交伴随 jet 的来源有限化与本篇是不同接口。

## 6. 已付与未付

已付：

- 所有 finite p-Schwartz 测试的完整 tame/p-primary 角色展开；
- 非法 $\mu_6$ 角色的原积分严格为零；
- 每个合法角色的准确公式 (20)，含 $\chi(34)^{-1}$ 和 $\theta^{11}$；
- 全局 $\rho_{k,\chi}$、两个 p-局部导子及2、3、17不分歧；
- 零值也服从同一身份；未作任何非消失假设。

仍未付：

- 任意有限 gate 来源都只含 $D_2,D_4$；本篇没有此断言；
- 原 (20) 对任意 p-ramified $\chi$ 的完整同周期点身份 (21)；
- 任意 companion 积分的系数自动属于 $\overline{\mathbf Q}$；
- 从这些有限行单独消去原 S/T/new 中央的真实外部补偿。

## 7. 来源

- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)，
  §§2–6：完整2/3/17有限角色、原两型五来源、全部正权平方、同周期普通测度；
  尤其其(30)–(35)是本篇(17)的唯一原算术输入。
- M. Bertolini, H. Darmon, K. Prasanna,
  *p-adic Rankin L-series and rational points on CM elliptic curves*,
  Pacific J. Math. 260 (2012), Theorem 3.1、Proposition 3.5及§3E。
  原 Katz 测度与 primitive 规范见该文；
  §3E 明写 p 与被固定角色导子互素，所以本篇不把其无分歧点定理直接套到 (21)。
  <https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf>
- Y. Liu, S. Zhang, W. Zhang,
  *A p-adic Waldspurger formula*, Duke Math. J. 167 (2018), 743–833，
  Definition 3.3.1、Theorem 3.3.2、Proposition 4.3.6及Appendix A。
  其任意有限深度的实际 point-period 身份用于说明§5的精确后续接口，
  本篇未把未识别的 local pairing 设为1。
  <https://web.math.princeton.edu/~shouwu/publications/pWalds.pdf>

本篇全部是对已付有界测度及有限角色的解析/代数证明，
不含数值扫描，不产生需入库的数据或证书。
