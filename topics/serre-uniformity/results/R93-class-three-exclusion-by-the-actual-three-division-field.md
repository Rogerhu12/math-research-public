# R93：以真实三除法域完全排除不分歧类数三分支

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文在 R91 的精确剩余角色和 R92 的实际整性上，加入同一椭圆曲线的三除法域。
两个残余候选在 $q=31$ 和 $q=139$ 分别产生矛盾，从而完成一个包含全部 $p>37$ 的明确子分支。
**不调用 Bajolet–Bilu–Matschke 的整点分类，不依赖其所被指出的证明缺口。**

## 1. 定理

设 $E/\mathbb Q$ 无 CM，$p>37$，且
$$
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).
$$
令 $K$ 为商二次域，$\lambda:G_K\to C\simeq\mathbb F_{p^2}^{\times}$ 为真实 Cartan 特征，
$\eta=\lambda^{(p^2-1)/3}$ 为 R66 的三次角色。

**定理 R93。** 以下三条件不能同时成立：
$$
\boxed{\lambda(I_p)=C^3,\qquad h_K=3,\qquad c(\eta)=1.}
\tag{93.1}
$$
因此原始环类数 $h(\mathcal O_c)=3$ 的实际小惯性分支，若存在，底域必有类数一，且
$$
(D,c)\in\{(11,2),(19,2),(3,6),(43,2),(3,9),(67,2),(163,2)\}.
\tag{93.2}
$$
这里没有对 (93.2) 声称存在性或排除；也不排除更大环类数和完整 Cartan 惯性。

## 2. 前序结果留下的准确对象

反设 (93.1)。R91 完整覆盖十六个类数三域与全部 $p>37$，给
$$
(D,p)=(643,47)\quad\text{或}\quad(907,47).
\tag{93.3}
$$
在 $s^2=-D$ 的有限域 $\mathbb F_{47^2}$ 中，取 R91 已固定的取向及素理想：

| $D$ | $q_0$ | $\mathfrak q_0^3=(\alpha_0)$ | $\nu(\mathfrak q_0)$，$\nu=\lambda^4$ |
|---:|---:|---|---|
|643|7|$\alpha_0=(27+\sqrt{-643})/2$|$35+5s$|
|907|13|$\alpha_0=(25+3\sqrt{-907})/2$|$25+14s$|

$\mathfrak q_0$ 取 $\alpha_0$ 消失的一支。
两种情况下 $\nu$ 在 $47$ 外不分歧，且有精确主理想公式
$$
\nu((\alpha))=\widetilde\alpha^{1476}.
\tag{93.4}
$$
R90 给实际环类数三的中心周期非零；R92 的 $p=47$ 整系数 Bézout 证书和 R72 的尖点判据遂给
$$j(E)\in\mathbb Z.
\tag{93.5}
$$
直到这一步尚未排除任何整点，不能直接引用存在异议的有限整点分类补上最后一步。
以下使用真实 $E[3]$，独立完成排除。

## 3. 整性与不分歧三次角色决定判别式的立方类

令 $\Delta_E\in\mathbb Z\setminus\{0\}$ 为全局最小判别式。

**引理 93.1（一般素数版本）。** 只假设 $p>37$、完整非分裂正规化子像、
$\lambda(I_p)=C^3$、$c(\eta)=1$ 和 $j(E)\in\mathbb Z$，不要求 $h_K=3$，则
$$
\boxed{\Delta_E\in p\mathbb Q^{\times3}\ \text{或}\ p^2\mathbb Q^{\times3}.}
\tag{93.6}
$$

**证明。** 整 $j$ 使 $E$ 在所有有限素数潜在好约化。
取有理素数 $q\ne p$，考虑 $T_p(E)$ 上的有限惯性像 $\Gamma_q$。
模 $p$ 约化在这个有限群上忠实，因为 $1+pM_2(\mathbb Z_p)$ 无非平凡有限阶元素。

若 $3\mid|\Gamma_q|$，Cauchy 定理给一个三阶元素。正规化子商的阶为二，所以该元素先落在
$C$，可由 $I_q\cap G_K$ 中元素提升。$c(\eta)=1$ 表示 $\eta$ 在 $K$ 所有有限点不分歧，
故这个元素必须落在 $\ker\eta=C^3$。但
$$
|C^3|=(p^2-1)/3
$$
素于三：R66 的小惯性已强迫 $p\equiv2,5\pmod9$。矛盾，故 $3\nmid|\Gamma_q|$。

在充分大的有限未分歧基变换后，杀掉有限惯性可取得一个好约化扩张，其绝对分歧指数 $e_q$
等于该有限惯性阶，特别 $3\nmid e_q$。不要求这一般的好约化扩张为循环或全分歧。
最小判别式在基变换及整模型缩放下满足
$$
e_qv_q(\Delta_E)=12m_q
$$
中的某个整数 $m_q$，因为扩张后的最小判别式赋值为零。于是
$$3\mid v_q(\Delta_E)\qquad(q\ne p).
\tag{93.7}
$$
这个 argument 直接涵盖 $q=2,3$ 的野约化，没有套用只适用于 $q\ge5$ 的 Kodaira 表。

在 $p$ 处，R66 已从精确小惯性证明最小好约化分歧指数为 $3$ 或 $6$。
所以 $3\nmid v_p(\Delta_E)$。也可不借完整 Kodaira 表证明最后一句：
若 $3\mid v_p(\Delta_E)$，取 $p$ 处极小短模型 $y^2=x^3+Ax+B$。
潜在好约化给 $3v_p(A)\ge v_p(\Delta_E)$，判别式恒等式又给
$2v_p(B)\ge v_p(\Delta_E)$。
令 $u=p^{v_p(\Delta_E)/12}$，缩放 $A/u^4,B/u^6$ 后模型整且判别式为单位。
$u$ 所需的分歧次数此时整除四，与最小次数 $3$ 或 $6$ 矛盾。

结合 (93.7)，判别式的立方自由部分只剩 $p$ 的指数一或二。符号 $-1$ 本身是有理立方，
不产生另一分支，证明 (93.6)。证毕。

## 4. 三除法的三次预解式及有限群条件

**引理 93.2。** 对特征零椭圆曲线 $y^2=x^3+Ax+B$，其 $3$ 挠点表示经
$$
\operatorname{GL}_2(\mathbb F_3)\longrightarrow S_3
$$
（核为四元数群 $Q_8$）的商，正是三次式
$$t^3+\Delta/27
\tag{93.8}
$$
的根置换表示，其中 $\Delta=-16(4A^3+27B^2)$。

**证明。** 四对非零 $3$ 挠点 $\{P,-P\}$ 的横坐标是首一四次式
$$
f_3(x)=x^4+2Ax^2+4Bx-A^2/3
\tag{93.9}
$$
的根 $x_1,x_2,x_3,x_4$。
群 $\operatorname{PGL}_2(\mathbb F_3)\simeq S_4$ 在这四个射影点上传递作用。
把四个点分成两对的三种方式，给三个预解式根
$$x_1x_2+x_3x_4,\quad x_1x_3+x_2x_4,\quad x_1x_4+x_2x_3.$$
直接以对称函数展开，它们的多项式为
$$
y^3-2Ay^2+(4A^2/3)y-8A^3/3-16B^2.
$$
代入 $y=t+2A/3$ 后恰得到 (93.8)。
对三种配对的作用是 $S_4\to S_3$，核为 Klein 四元群；在 $\operatorname{GL}_2(\mathbb F_3)$
中的逆像是 $Q_8$。因 $\Delta\ne0$，三预解式根互异，故根置换表示确为该商。
证毕。

由引理 93.1，其一般假设下真实曲线的这个商域必为
$$
\boxed{L_3=\mathbb Q(\zeta_3,\sqrt[3]{p}).}
\tag{93.10}
$$
使用全局短模型而非最小模型时，判别式只差十二次幂，不改变立方类。
$p$ 的一次、二次立方类给同一个分裂域。本定理的两个剩余候选取 $p=47$。

取 $q\ne3,p$、$q\equiv1\pmod3$。$L_3$ 在 $q$ 不分歧，且有
$$
\operatorname{Frob}_q|_{L_3}=1
\quad\Longleftrightarrow\quad p^{(q-1)/3}\equiv1\pmod q.
\tag{93.11}
$$
不等于一时，它在 $S_3$ 中为三循环。

**引理 93.3。** 设 $\widetilde E/\mathbb F_q$ 的迹为 $a$，$q\equiv1\pmod3$。
记 $M$ 为其 Frobenius 在 $\widetilde E[3]$ 上的矩阵。

- 若 $M\in Q_8$，则
  $$a\equiv0\pmod3\quad\text{或}\quad a\equiv\pm(q+1)\pmod9.$$
- 若 $M\in\operatorname{SL}_2(\mathbb F_3)\setminus Q_8$，则 $3\nmid a$。

**证明。** $\det M=q=1$ 于 $\mathbb F_3$。
$Q_8$ 的六个非中心元素均有阶四、迹零；两个中心元素为 $I,-I$。
若 $M=I$，全部 $3$ 挠点有理，故 $9\mid\#\widetilde E(\mathbb F_q)=q+1-a$。
若 $M=-I$，一个非平方二次扭曲的 Frobenius 为 $I$，故 $9\mid q+1+a$。
这证明第一条。
$\operatorname{SL}_2(\mathbb F_3)$ 中任意迹零矩阵满足 $M^2=-I$，恰为上述六个非中心元素，
所以群外元素不可能迹零，证明第二条。
证书还完整枚举 $48$ 个可逆矩阵、其四射影点和三配对作用，独立核对这些群事实。
证毕。

## 5. 同一个实际 Frobenius 同时接受模 47 与模 3 约束

下面取 $q$ 在 $K$ 分裂，且 $q\not\equiv1\pmod{47}$。
R63 在 $q$ 给**循环全分歧**好约化扩张，剩余域仍为 $\mathbb F_q$；这与引理 93.1
对一般素数只要求有限分歧指数的步骤不同。
在该扩张中取实际好约化 $\widetilde E/\mathbb F_q$，记其整数迹为 $a$。

模 $47$ 的根 $\beta$ 满足
$$
\operatorname{Tr}(\beta)=a\pmod{47},\quad N(\beta)=q\pmod{47},
\quad\beta^4=\nu(\mathfrak q),\quad |a|\le2\sqrt q.
\tag{93.12}
$$
同时，$L_3/\mathbb Q$ 在 $q$ 不分歧。改变 Frobenius 提升只乘惯性，或改在这个全分歧扩张上
取 Frobenius，都不改变其 $S_3$ 商值。因此**同一个 $a$** 必须满足引理 93.3，
其分支由 (93.11) 决定。这里不能在两个模特征上独立选两条有限域曲线。

### 5.1 $D=643$：在 $q=31$ 的矛盾

令 $s^2=-643\pmod{47}$。取
$$
\gamma=(15+\sqrt{-643})/2,\qquad N\gamma=7\cdot31.
$$
$\mathfrak q_0$ 的剩余根为 $r_0=-27=1\pmod7$，
$15+r_0\not\equiv0$、$15-r_0\equiv0\pmod7$，
所以 $(\gamma)=\mathfrak q\bar{\mathfrak q}_0$，其中 $\mathfrak q\mid31$。
R91 的主理想关系精确给
$$
\nu(\mathfrak q)=\widetilde\gamma^{1476}(35+5s)/7^4=43+12s.
\tag{93.13}
$$
在 $\mathbb F_{47^2}$ 完整求满足 (93.12) 的四次根，并保留整数 Hasse 区间，得到
$$a\in\{-10,10\}.
\tag{93.14}
$$
另一方面，$31\equiv1\pmod3$ 且
$$47^{10}\equiv1\pmod{31}.$$
于是 Frobenius 的三次商平凡，(93.14) 须满足
$$a\equiv0\pmod3\quad\text{或}\quad a\equiv\pm32\pmod9.$$
$\pm10$ 均不被三整除，模九为 $1,8$，而 $\pm32$ 模九为 $5,4$，矛盾。

### 5.2 $D=907$：在 $q=139$ 的矛盾

令 $s^2=-907\pmod{47}$。取
$$
\gamma=(60-2\sqrt{-907})/2,\qquad N\gamma=13\cdot139.
$$
$\mathfrak q_0$ 的剩余根为 $r_0=-25/3=9\pmod{13}$。
$60-2r_0\not\equiv0$、$60+2r_0\equiv0\pmod{13}$，
所以仍有 $(\gamma)=\mathfrak q\bar{\mathfrak q}_0$，$\mathfrak q\mid139$。
准确角色值为
$$
\nu(\mathfrak q)=\widetilde\gamma^{1476}(25+14s)/13^4=44+27s.
\tag{93.15}
$$
(93.12) 的完整整数迹列表为
$$a\in\{-12,-6,6,12\}.
\tag{93.16}
$$
但 $139\equiv1\pmod3$，且
$$47^{46}\equiv42\not\equiv1\pmod{139}.$$
三次商是非平凡三循环，引理 93.3 要求 $3\nmid a$，与 (93.16) 矛盾。
两对全部排除，定理 R93 得证。

## 6. 精确证书与范围

运行

```bash
python -B scripts/verify_class_three_mod3_exclusions.py
```

源码只用 Python 标准库，调用 R91 的有限域整数实现。
它重建两条范数及理想分支关系，计算实际 $\nu$ 值，枚举全部整数 Hasse 迹及所有有限域根，
验证两次立方剩余测试，并完整枚举 $\operatorname{GL}_2(\mathbb F_3)$ 的配对商。
两个最后的交集均严格为空。

数据 `scripts/data/class_three_mod3_exclusions.json` 的 SHA256：

```text
17fa3b4d79f6af79f75b17eb330a84d0141e7328975b2471f67a439bdf6fc02a
```

R93 的无限素数量词由 R91 的非零整数整除证书负责，最后两个固定素数只用于排除全部剩余者。
它不是从有限局部窗口猜测全局满像；必要条件同时来自真实 $E[47]$、真实 $E[3]$ 和实际整性。
R92 中保留的 BBM 问题在此没有作为输入。

由 R90 的原始环类数三分类，$h_K=3$ 必有 $c=1$，已经排除；$h_K=1$ 只余 (93.2)，
证明定理后的推论。更大类数、分歧三次角色和完整惯性仍是本课题的开放主线。

内部证明输入：
[R63](R63-all-prime-classes-and-quotient-discriminant-growth.md) §§2–3；
[R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md) §§2–4；
[R90](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)；
[R91](R91-unramified-cubic-class-number-three-prime-bound.md)；
[R92](R92-small-level-fourier-units-and-actual-integrality.md)。
