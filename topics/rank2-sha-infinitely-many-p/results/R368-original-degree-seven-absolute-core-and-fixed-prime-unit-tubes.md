# R368：原 degree 七的绝对 core 与固定普通素数族上的碰撞单位

日期：2026-11-13。**状态：以下完整 degree 七作用、原 $D_7$ 的绝对
core，以及固定普通素数族上的实际碰撞质量单位均已证明。**
绝对标量由同一个 degree 七空间中的原 $\sigma(\gamma_7z)$ 锚定；
不以项目 Weil 表示或有限个素数试验确定符号。
本结果补上 R362 中的实际 $\lambda_7$，不证明原中央导数非零，
也不把尚未完成的 R364 两条 Faber 行登记为已解决。

## 1. 原来源、单位与主结论

沿用 R316、R358、R362 的规范：
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad b=17,\quad E_b:y^2=x^3+b,
$$
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad\Theta=x\sigma^2,\quad C=y\sigma^3.
$$
本篇的来源是 R362 的原相位 $\omega,\omega^2$：
$$
\boxed{D_7=-\Theta^2C=-\sigma^7x^2y,\qquad D_7(0)=1.}
\tag{1}
$$
它在同一个 $\sigma^7L(7O)$ 中，是 $\mu_6$ 型零的唯一线。

固定普通 $p>7$，保持实际 CM type：
$$
\pi=\psi_{17}(\mathfrak p),\quad
\pi_0=\psi_0(\mathfrak p)=\varepsilon\pi,\quad
\pi_0\bar\pi_0=p,\quad
v_{\mathfrak p}(\pi_0)=1,\quad v_{\mathfrak p}(\bar\pi_0)=0,
$$
$$
\varepsilon\in\mu_6,\qquad
\bar\pi_0=\varepsilon^{-1}\bar\pi,\qquad
\kappa=p/\bar\pi^2.
\tag{2}
$$
这里 $\psi_0$ 是 $E_0:y^2=x^3+1$ 的原角色。
其已付的 primary 规范是
$$\pi_0\equiv1\pmod{2\delta};$$
不能用任意范数 $p$ 生成元代替它。

因为七在 $K$ 中分裂，存在唯一
$$
\boxed{
u_p\in\mu_6,\qquad
u_p\equiv\pi_0/\bar\pi_0\pmod{7\mathcal O_K}.
}
\tag{3}
$$
分母在模七可逆，因 $p\ne7$。以下常写 $u=u_p$，并置
$$\chi_2(p)=\left(\frac2p\right).$$

**定理。** 同一个原 Amice 测度满足
$$
\boxed{
\nu_{D_7}|_{p\mathbf Z_p}
=\lambda_7[\kappa]_*\nu_{D_7},\qquad
\lambda_7=\frac{\varepsilon u}{\bar\pi}
          =\frac u{\bar\pi_0}.
}
\tag{4}
$$
原 $F_{23}=\sigma(2z)\sigma(\delta z)$ 的完整 core 同时为
$$
\boxed{
\lambda_{23}=\frac{\varepsilon^5u^{-1}}{\bar\pi},\qquad
\lambda_{23}\lambda_7=\lambda_\sigma^2=\bar\pi^{-2}.
}
\tag{5}
$$
令 R362 的整个二维 core 为
$$
\lambda_\Xi=\lambda_K\lambda_D
 =\frac{\varepsilon^2\chi_2(p)}{\bar\pi^2}
 =\frac{\chi_2(p)}{\bar\pi_0^2}.
\tag{6}
$$
则在固定素数族
$$
\boxed{
\mathcal P_7=
\{p>7:\ p\equiv1\pmod3,\quad (-14/p)=1\}
}
\tag{7}
$$
上，有
$$\boxed{\lambda_7-\lambda_\Xi\in\mathcal O_{\mathfrak p}^{\times}.}\tag{8}$$
该族包含所有 $p\equiv1\pmod{168}$ 的素数，因而是一个无穷的固定
普通素数族。额外地，对任何当前普通素数，只要 $u=\pm1$，(8)
也成立。

这些结论只支付原辅助的质量系数；没有给未知原 $J'_S(0)$ 赋值。

## 2. 奇 degree 的真实 trace 与原半特征

先在 $b=1$ 工作，暂省略零下标。设
$$
\mathcal S_7=\sigma^7L(7O),\qquad \dim\mathcal S_7=7.
$$
对奇范数 CM 元素 $a$，沿用带首项常数 $a$ 的原 division 函数
$$r_a(z)=\frac{\sigma(az)}{\sigma(z)^{Na}},\qquad Na=a\bar a.$$
它是真椭圆函数。除了
$\eta_{a\lambda}=\bar a\eta_\lambda$ 消去指数因子外，
还须保留 sigma 的奇半特征：
在 $\Gamma/2\Gamma$ 上，唯一 odd 二次特征对每个可逆线性变换
不变；奇范数的 $a$ 恰给这种变换。
因此 $\chi(a\lambda)=\chi(\lambda)=\chi(\lambda)^{Na}$。
没有把奇 degree 偷换成偶 degree 的平坦线丛。

定义不除以 $Na$ 的实际迹
$$
\boxed{
\mathscr M_a(\sigma^7f)
=\sigma^7\operatorname{Tr}_{[a]}
 \left[\left(\frac{r_{\bar a}}{r_a}\right)^7
              f\circ[\bar a]\right].
}
\tag{9}
$$
括号内的极点至多是 $7[a]^*(O)$，同源在特征零无分歧，
故输出仍在 $\mathcal S_7$。
R300 的完整正式群根单位平均在这里逐项仍适用：
使用的是相同 division 身份的第七次幂，不需要 $7$ 为偶数。
于是同一测度的真实算子为
$$
\boxed{
T_{p,0}=\frac{\bar\pi_0}{p}\mathscr M_{\pi_0}
       =\pi_0^{-1}\mathscr M_{\pi_0}.
}
\tag{10}
$$
原整性也可直接看出：$\sigma(\log_Et)\in t\mathcal O[[t]]$，
标准 $x,y$ 展开与下列七个极阶都给整正式级数。
(10) 没有留下新的平方根或未定的 $p$ 因子。

## 3. order-seven 与对称性共同给唯一 lift

本节明确支付奇 degree 的中心；不能仅从模七的项目矩阵下结论。

令 $\mathsf JG(z)=G(-z)$，使 $\mathsf J^2=1$。
对每个 $T\in E[7]$，从原 theta 群取任一 lift $A_T$。
写
$$
A_T^7=a\,\mathrm{id},\qquad
\mathsf JA_T\mathsf J=b\,A_T^{-1}.
$$
两式给 $b^7=a^2$。令
$$\widetilde A_T=(b^3/a)A_T.$$
则直接计算
$$
\widetilde A_T^7=1,\qquad
\mathsf J\widetilde A_T\mathsf J=\widetilde A_T^{-1}.
\tag{11}
$$
若另一个 lift 也满足 (11)，它与本 lift 相差 $\zeta\in\mu_7$；
对称性又给 $\zeta^2=1$。因为七为奇数，$\zeta=1$。
故 (11) **共同**确定唯一 lift。单独的 order-seven 条件并不唯一。

记此实际 lift 为 $U_T$。这只是规范 theta 群的标量，不更换
原截面 $\sigma^7f$，也不改变 (9)、(10) 的原标量。
特别没有将原半特征或一个偶半周期常数隐去。

对一组辛基 $T_1,T_2$，$U_{T_1},U_{T_2}$ 的交换子是 primitive
七次根。先取 $U_{T_1}$ 的一个特征向量，再用 $U_{T_2}$ 循环，
得到七个不同特征值。因此这七维表示不可约。

## 4. 真正的交织方向及绝对锚

在原几何迹 $[a]_*[\bar a]^*$ 中，theta 群的底层参数变成
$$T\longmapsto a\bar a^{-1}T.$$
这是 R300 (16) 的同一方向。
在奇 degree 上，先用完整 Gaussian lift 做支的换元，
可得 $\,\mathscr M_aU_T=c\,U_{a\bar a^{-1}T}\mathscr M_a\,$，
其中 $c$ 是中心标量。原 division 函数在奇范数下为偶函数，
所以 (9) 与 $\mathsf J$ 交换。两 lift 的七次幂给 $c^7=1$，
再应用 $\mathsf J$ 并用 (11) 的逆式给 $c^2=1$。
当算子非零时（下方 (15) 独立保证本篇所用算子非零），于是 $c=1$。
因此
$$
\boxed{
\mathscr M_aU_T=U_{a\bar a^{-1}T}\mathscr M_a.
}
\tag{12}
$$
这一论证保留了原周期常数；只用项目交织不足以得出 (12)。

对 $v\in\mu_6$ 定义实际曲线自同构
$$\mathsf I_vG(z)=G(vz).$$
它与 $\mathsf J$ 交换，并同样由 (11) 得到
$$\mathsf I_vU_T=U_{v^{-1}T}\mathsf I_v.\tag{13}$$

现在 $\mathcal O_K/7\simeq\mathbf F_7\times\mathbf F_7$，
可取 $\omega\mapsto(2,4)$。
其 norm-one 群有六个元素，而原 $\mu_6$ 正好给全部元素：

| 原单位 $v$ | 第一分量 | 第二分量 |
|---|---:|---:|
| $1$ | $1$ | $1$ |
| $-\omega^2=1+\omega$ | $3$ | $5$ |
| $\omega$ | $2$ | $4$ |
| $-1$ | $6$ | $6$ |
| $\omega^2$ | $4$ | $2$ |
| $-\omega$ | $5$ | $3$ |

这证明 (3) 的存在与唯一性。
由 (12)、(13)，$\mathscr M_{\pi_0}$ 与 $\mathsf I_{u^{-1}}$
有完全相同的 Heisenberg 交织。

取原
$$\gamma_7=3+\omega=(5+\delta)/2,\qquad N\gamma_7=7.$$
实际同 degree 截面
$$A_\gamma(z)=\sigma(\gamma_7z)=r_{\gamma_7}(z)\sigma(z)^7$$
非零，并且
$$A_\gamma(vz)=vA_\gamma(z)\qquad(v\in\mu_6).\tag{14}$$
R316 已付 $T_{p,0}\nu_\sigma=\nu_\sigma$。
因为 $\gamma_7$ 在当前普通处是单位，完整 $p$ 限制、
支撑除以 $p$ 及单位缩放都与 $[\gamma_7]_*$ 交换。
所以是在同一原测度上准确得到
$$
\boxed{
T_{p,0}A_\gamma=A_\gamma,\qquad
\mathscr M_{\pi_0}A_\gamma=\pi_0A_\gamma.
}
\tag{15}
$$
这里没有用 $A_\gamma$ 的某个未知 Mellin 值去作除法。

(15) 保证 $\mathscr M_{\pi_0}$ 非零。
不可约性和 Schur 引理使
$\mathscr M_{\pi_0}=c\,\mathsf I_{u^{-1}}$。
在 (14)、(15) 的同 degree 真锚上求 $c$，唯一得到
$$
\boxed{
\mathscr M_{\pi_0}=\pi_0u\,\mathsf I_{u^{-1}},
\qquad T_{p,0}=u\,\mathsf I_{u^{-1}}
\quad\hbox{于整个 }\mathcal S_7.
}
\tag{16}
$$
因此无需先证明不同范数迹的抽象乘法，也无需从有限几个生成元
猜一个绝对角色。

## 5. 完整七维表与 $E_{17}$ 的原周期

标准七维基及其实际 $\mu_6$ 型为下表。
型 $k$ 表示 $G(vz)=v^kG(z)$：

| $f$，其中 $G=\sigma^7f$ | 极阶 | $k\bmod6$ | $T_{p,0}$ 的标量 |
|---|---:|---:|---:|
| $1$ | $0$ | $1$ | $1$ |
| $x$ | $2$ | $5$ | $u^2$ |
| $x^2$ | $4$ | $3$ | $u^4$ |
| $x^3$ | $6$ | $1$ | $1$ |
| $y$ | $3$ | $4$ | $u^3$ |
| $xy$ | $5$ | $2$ | $u^{-1}$ |
| $x^2y$ | $7$ | $0$ | $u$ |

两条 type-one 来源构成二维锚块；表中没有将它误计为一维。

令 $\theta=17^{1/6}$，使用原
$\Omega_{p,0}=\theta\Omega_p$、$x_b(z)=\theta^2x_0(\theta z)$、
$\sigma_b(z)=\theta^{-1}\sigma_0(\theta z)$。
一般表中单项式只添固定非零 $\theta$ 次幂；
该因子在完整 core 两边相同。
原缩放参数为
$$p/\bar\pi_0^2=\varepsilon^2\kappa.$$
对型 $k$ 的原测度有
$[\varepsilon^2]_*\nu_G=\varepsilon^{2k}\nu_G$。
故 (16) 的完整原限制是
$$
\boxed{
\nu_G|_p=
\frac{\varepsilon^{2k+1}u^{\,1-k}}{\bar\pi}
                   [\kappa]_*\nu_G.
}
\tag{17}
$$

特别 $D_{7,b}(z)=D_{7,0}(\theta z)$、$k=0$，得到 (4)。
而
$$F_{23}=-2\delta\sigma^7xy,\qquad k=2,$$
得到 (5)。这也与 R362 真两输入联合所付的
$\lambda_{23}\lambda_7=\lambda_\sigma^2$ 完全吻合。
(17) 始终是整个测度式，含原所有 tame 分支。

## 6. 原有限相位的立方与整数迹的模三

写 $\pi_0\bmod7=(a,b)$，其中 $a,b\in\mathbf F_7^\times$，
$ab\equiv p\bmod7$。由 (3)，$u$ 的第一分量为 $a/b$。
因此
$$
(a/b)^3=a^3b^3=(ab)^3=\left(\frac p7\right)\pmod7.
$$
这里用 $b^6=1$。原 $u^3$ 本来在 $\{\pm1\}$ 中，故
$$\boxed{u^3=(p/7).}\tag{18}$$

置
$$\tau=u\bar\pi_0,\qquad a_\tau=\tau+\bar\tau\in\mathbf Z.$$
它是实际代数整数，范数为 $p$，所以
$$|a_\tau|\le2\sqrt p.\tag{19}$$
这里只用复共轭和范数；无需把 $\tau$ 认作某条未经识别的
椭圆曲线的 Frobenius。

primary 规范给 $\pi_0,\bar\pi_0\equiv1\bmod\delta$。
又在 $\mathcal O_K/(\delta)=\mathbf F_3$ 上
$u\equiv u^3$。若 $\alpha=A+B\omega$，则
$$\operatorname{Tr}\alpha=2A-B\equiv2(A+B)\pmod3.$$
于是
$$
\boxed{a_\tau\equiv2u^3\pmod3.}
\tag{20}
$$
这保留了原 primary 单位；若随意将 $\pi_0$ 乘一个六次单位，
(20) 会随之改变。

## 7. 实际碰撞差的单位证明

由 (4)、(6)，
$$
\boxed{
\lambda_7-\lambda_\Xi
=\frac{u\bar\pi_0-\chi_2(p)}{\bar\pi_0^2}.
}
\tag{21}
$$
假设其非单位。因为
$\bar\tau=u^{-1}\pi_0$ 被所选 $\mathfrak p$ 整除，(21) 给
$$a_\tau\equiv\chi_2(p)\pmod p.$$
对本篇 $p>7$，(19) 有 $2\sqrt p<p-1$，所以整数范围只容许
$$a_\tau=\chi_2(p)\in\{\pm1\}.\tag{22}$$

若 $\chi_2(p)=u^3$，则 (20) 与 (22) 给
$u^3\equiv2u^3\bmod3$，矛盾。
由 (18) 及二次互反
$$
\chi_2(p)u^3=(2/p)(p/7)=(-14/p),
$$
故 (7) 恰保证 $\chi_2(p)=u^3$。
这完整证明 (8)，没有把一个模 $p$ 等式未经整数界就提升为 (22)。

若 $u=\pm1$，则 $a_\tau=\pm(\pi_0+\bar\pi_0)$。
因为 $\pi_0\equiv1\bmod2$，这个整数为偶数，
同样不可能等于 (22) 的奇数。故额外判据也已证明。

另有一个可直接使用的原单来源边界：
$$
\boxed{
1-\lambda_7\in\mathcal O^\times
\quad\hbox{若 }(p/7)=1\ \hbox{或 }u=\pm1.
}
\tag{23}
$$
证明把上面的 $\tau$ 换为 $u^{-1}\bar\pi_0$。
其迹模三仍为 $2u^3$；若 $1-\lambda_7$ 非单位，
同一整数界迫该迹为一。当 $u^3=1$ 时与模三矛盾；
$u=\pm1$ 时由偶性排除。
特别在固定无穷子族 $p\equiv1\bmod168$ 上，(8)、(23) 同时成立。

对于任何已由原联合给出的比值
$$
\lambda_{\rm quot}:=\lambda_\Xi/\lambda_7
=\frac{\chi_2(p)}{u\bar\pi_0},
$$
也立即有
$$
\boxed{
1-\lambda_{\rm quot}
=(\lambda_7-\lambda_\Xi)/\lambda_7\in\mathcal O^\times
\quad(p\in\mathcal P_7).
}
\tag{24}
$$
(24) 只使用已付实际比值；没有擅自给比值来源指定另一条曲线身份。

## 8. R362 两个原相位的全部质量与真正中央返回

R362 的两个相位 $\zeta=\omega,\omega^2$ 都有来源 $D_7$。
因此对全部 $N\ge0$，准确有
$$d_{\zeta,N}=\lambda_7^N.$$
对 $N\ge a\ge1$，其实际双深度及 unit 碰撞管质量成为
$$
\boxed{
e_{\zeta;a,N}=\lambda_\Xi^a\lambda_7^{N-a},\qquad
q_{\zeta,N}
=(\lambda_7-\lambda_\Xi)\lambda_7^{N-1}.
}
\tag{25}
$$
在 (7) 的所有素数和全部 $N\ge1$ 上，
$q_{\omega,N},q_{\omega^2,N}$ 均为单位。

两个真实 primitive 输入规范也完整保留：
$$
\boxed{
e_{\zeta;a,N}^{\rm prim,j}
=(\lambda_\Xi-t_p^j)\lambda_\Xi^{a-1}\lambda_7^{N-a},
\qquad j=3,5.
}
\tag{26}
$$
这里 $t_p=\varepsilon^3p/\bar\pi^3$。
因 $v_p(t_p)=1$，(26) 对所有本篇普通素数都是单位；
它不是可删除的双非单位输出尾。

(25) 的系数与 Mellin 权无关。
所以 R362 同一原联合在合法辅助管上，保全部原 tame $\ell$，
准确给
$$
\boxed{
J_{\mathcal H_{\zeta,N};\ell}(v)
=q_{\zeta,N}J_{S,\ell}(v),\qquad
J'_{\mathcal H_{\zeta,N};\ell}(0)
=q_{\zeta,N}J'_{S,\ell}(0).
}
\tag{27}
$$
此处原输出没有被重新缩放，因此不额外添参考斜率。

如果将 $D_7$ 自身第 $n$ 个环带除以 $p^n$ 归一，则仍须保
$d=p-1$ 下的完整式
$$
M_{7,\ell}^{[n]}(v)
=\lambda_7^n\omega_p(\bar\pi)^{-2n\ell}
 \langle\bar\pi\rangle^{-2ndv}M_{7,\ell}(v),
\tag{28}
$$
以及导数中的
$-2nd\log_p(\bar\pi)M_{7,\ell}(0)$。
原质量为 $M_{7,0}(0)=1-\lambda_7$；不能把它自动当零。

由于 $\lambda_7$ 为单位，完整测度的有限层重构仍是
$$
\nu_{D_7}
=\sum_{n=0}^{M-1}\lambda_7^n[\kappa^n]_*\nu_{D_7}^{\times}
 +\lambda_7^M[\kappa^M]_*\nu_{D_7}.
\tag{29}
$$
最后一项质量为 $\lambda_7^M$，不可删去。

本结果支付 (27) 的无损系数。R362 的原单叶域仍含
$Y_A-\xi\delta L\in p^N$ 的部分输出条件和六个真实分支；
其 unit 中心平移小球四项仍全部保留。因此 (27) 不等同于
原单叶域或 R339 独立深度族的免费零传播。

## 9. 有限核对与依赖

第4节表给出全部六个 norm-one 元素；对模七的全部三十六个
可逆 $a$，直接在
$(A+B\omega)(C+D\omega)=(AC-BD)+(AD+BC-BD)\omega$
中检查，$a/\bar a$ 总在这六元表，且其立方恰为 $(Na/7)$。
这项固定有限核对已在 JavaScript 有限域运算中全部通过。
全素数结论的证明是 §§2–7 的实际交织、同 degree 锚和整数迹，
不来自目标素数扫描。

- [R302：原 $E_0$ 与 primary Hecke 规范](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)。
- [R300：原 trace、正式群平均与完整 Heisenberg 交织方向](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)，§§2–2.1；
  本文第2、3节支付其在奇 degree 七的半特征与中心。
- [R316：同一原 sigma 的完整 core 与普通周期](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R345：奇 order 与对称 lift 的原 degree 三先例](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)；
  本文第3节独立给出 order-seven 的完整唯一性证明。
- [R358：原 $D,K$ 的绝对 core](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)。
- [R362：原三输入、两输入与六相位的完整联合](R362-original-triple-pair-core-and-six-branch-leaf-domain.md)，特别 §§5、9–10。

本文以 GitHub Contents API 提交小文本，没有声称执行本地 git pull。
提交前两 README 的内容 blob 仍为
f787a306d90892d8dec765dc59747d60ba39f055、
f8dd8071ac0c2b31f344a40c15ac2a42796bf9af，
与已读基准 35e391cd9a73d5a514d252312d3ff61962ddbc70 相同。
