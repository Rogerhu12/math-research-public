# R150：全余 W 的同一原均值理想中的首一物理 λ 六次式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 结论与适用域

在既有一般 LS、$\Delta=0$、$W=0$ 原物理余图上，令 $A_W$ 为仅对已经独立支付的权因子局部化的 $\mathbb Q[e,k]$。沿用

$$
u=e+1,\quad Q=ek,\quad V=uk+2,\qquad
\ell=\frac{u((k+2)^2-2ek)}{kV}.
$$

记原四个二次均值为

$$
F_4=(E_1,E_{Be},E_{Bo},N_1)^T,\qquad
I_4=(E_1,E_{Be},E_{Bo},N_1)
\subset A_W[x,y,t].
\tag{1}
$$

**定理。** 下文同一个原乘法矩阵明确地定义

$$
\chi_\lambda(Z)=\det(ZI_6-M_\lambda)
=Z^6+c_1Z^5+\cdots+c_6\in A_W[Z],
\tag{2}
$$

并给出完整原理想身份

$$
\chi_\lambda(\lambda)
=\varepsilon_0^T\operatorname{adj}(\lambda I_6-M_\lambda)E_\lambda F_4
\in I_4.
\tag{3}
$$

这里 $\varepsilon_0=(1,0,0,0,0,0)^T$，$\lambda$ 是同一点的物理值坐标，不是另选的六阶矩阵参数。式 (2) 的最高系数恰为 1；没有未付的 $\lambda$ 首项零纤维。所有 $c_j$ 的分母仅来自既有已付权量，式 (3) 不使用几何 $D$ 的逆。

这是对全余 W 有效的一个具体首一原条件。它不把全部必要方程改称完整原系统的充分条件，不宣称 W 已空，也不将六个生成元假定成自由基底。这里的六生成性此前已刊，不作为新的有限性成果重复登记。

## 2. 已刊全域六规则的准确来源

使用[全 W 原 NS/PS 固定六行定理](R150-appendix-unit211-W-entire-original-native-NSPS-necessary-weight-curve.md)第 2–3 节的同一原坐标、六规则与 18 条实际乘法身份。其原六式为

$$
(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
$$

四个二次头按 $x^2,xy,xt,y^2,yt,t^2$ 排列，选列 $[0,1,2,5]$；固定两个原 overlap 行 $[0,2]$ 再给出 $y^3,y^2t$ 的首一规则。首一头为

$$
x^2,\ xy,\ xt,\ t^2,\ y^3,\ y^2t.
\tag{4}
$$

这些规则的原迹均只用前四个原式。具体构造是：前四条为四个原二次的伴随逆组合，后二条为前四条的原 overlap 及其二次约化的组合。因此六条迹在 $N_S,P_S$ 两个位置的系数恒为零；并没有从加权 N/P 新增任何假定来获得 (4)。

旧源曾显式保留 $(k+2)J_{19}C_9\ne0$。它们现在分别由以下完整原结论支付：

- [一般等权完整排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，结合 $(\ell-u)kV=u(k+2)(2-Q)$，支付 $k+2$；
- [整个 J19 原权曲线排除](R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)；
- [整个 C9 原权曲线排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)。

其余原头因子均在同一既有权单位表中。上述全域定理已实际核过真实二次头、三次头的分子与分母和所有矩阵分母，不以旧源码中的图标签代替证明。这里不使用尚未排除的 $H_{265}$，不把 $D_{27}$、$J_{19}$ 或 $G_{36}$ 的名称偷换成 C9 的单位来源。

固定列为

$$
v=(1,x,y,t,y^2,yt)^T.
\tag{5}
$$

六规则按已刊固定单项式序严格降低几何单项式，故 $A_W[x,y,t]/I_4$ 由 (5) 生成；重叠可能带来进一步关系，不影响生成性。

对 $\xi=x,y,t$，同一规则约化每个 $\xi v_i$，完整保留四项原组合，给

$$
\xi v-M_\xi v=E_\xi F_4,
\tag{6}
$$

其中

$$
M_\xi\in\operatorname{Mat}_6(A_W),\qquad
E_\xi\in\operatorname{Mat}_{6\times4}(A_W[x,y,t]).
$$

矩阵方向是行作用于真实值列。此前执行已经逐项返回全部 18 条 (6)。把原六项迹缩成四项，是因为末两项按构造恒为零，不是删去未知项。后续源也显式保留这两个零检查。

## 3. 同一点的物理 λ 仿射恢复

沿用原 $E_0,N_0,P_1$ 恢复。令

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P_{02}=(2-3u)V_2-Qu+2u^3.
$$

则

$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$

$$
\lambda=
\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P_{02}}.
\tag{7}
$$

将第一式代入第二式得到

$$
\lambda=\alpha_0+\alpha_xx+\alpha_yy+\alpha_tt,
\tag{8}
$$

其中

$$
\alpha_0=\frac{T_0^2}{4uP_{02}},\qquad
\alpha_x=\frac{T_0}{2P_{02}},\qquad
\alpha_t=\frac{bcQ}{P_{02}},
$$

$$
\alpha_y=\frac{2u-uQ-\ell Q-(V_2+2u^2)(u-\ell Q)/(2u)}{P_{02}}.
\tag{9}
$$

所有系数均属 $A_W$，$\alpha_t$ 为既有原权单位。这里的 $bc$ 由 $4bc(1-Q)=\ell(2u-\ell Q)-u^2$ 恢复，是权环中的元素。

定义

$$
M_\lambda=\alpha_0I_6+\alpha_xM_x+\alpha_yM_y+\alpha_tM_t,
$$

$$
E_\lambda=\alpha_xE_x+\alpha_yE_y+\alpha_tE_t.
\tag{10}
$$

把三组 (6) 分别乘对应 $\alpha$ 后相加，逐列恰得到

$$
(\lambda I_6-M_\lambda)v=E_\lambda F_4.
\tag{11}
$$

式 (11) 的 $\lambda$ 就是 (7) 的原物理值。没有独立选择矩阵特征值，也不需要假设 $M_x,M_y,M_t$ 在无关系的六维自由空间上彼此交换。

## 4. 伴随矩阵的原理想返回

任意交换环上的方阵均有多项式身份

$$
\operatorname{adj}(ZI_6-M_\lambda)(ZI_6-M_\lambda)
=\det(ZI_6-M_\lambda)I_6.
\tag{12}
$$

这里可以在自由多项式矩阵环 $A_W[Z]$ 中形成 (12)，再将 $Z$ 代成 (8)。左乘 (11) 并取第 0 行，因 $v_0=1$，即得

$$
\begin{aligned}
\chi_\lambda(\lambda)
&=\varepsilon_0^T
\operatorname{adj}(\lambda I_6-M_\lambda)
(\lambda I_6-M_\lambda)v\\
&=\varepsilon_0^T
\operatorname{adj}(\lambda I_6-M_\lambda)E_\lambda F_4.
\end{aligned}
\tag{13}
$$

这是在原多项式环中的等式，而非仅在原点的数值零断言。其四个原乘子由 (10)、(12) 明确定义，不要求展开并保存大系数。

式 (12) 关于形式 $Z$ 的最高项为 $Z^6$。因此 (2) 必为首一六次，且全部系数由 $A_W$ 的有限次加法、乘法取得。没有除以任何新的权参数首项，也没有除以 $\lambda$ 或 $D$。

六个 $v_i$ 可以有关系，甚至某些权纤维上实际生成数下降；(13) 仍然逐项成立。自由的是写 (12) 时的形式矩阵坐标空间，不是断言原商的六个元素自由。

## 5. 新显式构造及其边界

新冻结源只执行旧 C9 源中形成四二次、六规则与 18 条 (6) 的必要前缀。它不执行旧 NS/PS 余式、交换子、自适应 Gaussian、大权行列式或已冻结的 12 阶 Sylvester 门。

在实际返回六条 (11) 后，源取 $M_\lambda$ 全部系数分母的最小公倍数 $\delta\in A_W^\times$，核

$$
N=\delta M_\lambda\in\operatorname{Mat}_6(\mathbb Q[e,k])
\tag{14}
$$

的全部 36 项，并按原已付表支付 $\delta$。随后所有矩阵乘法在多项式权环进行。设

$$
B_0=I_6,\qquad
d_j=-\frac1j\operatorname{tr}(NB_{j-1}),\qquad
B_j=NB_{j-1}+d_jI_6\quad(1\le j\le6).
\tag{15}
$$

Faddeev–LeVerrier 身份给

$$
\det(ZI_6-N)=Z^6+d_1Z^5+\cdots+d_6,\qquad B_6=0,
$$

$$
c_j=d_j/\delta^j.
\tag{16}
$$

源逐项核 (15)，最后要求 $B_6$ 的全部 36 项确为零。$B_j/\delta^j$ 都是同一个 $M_\lambda$ 的多项式，故对应伴随多项式与 $M_\lambda$ 交换。此处只用单矩阵多项式的交换性，完全不用三个坐标乘法矩阵的自由交换性。

这些显式系数运算是后续原输入的构造，不是对已完成纸面证明 (13) 追加执行门。冻结时新源尚未执行，本稿不声称已经得到新运行的全部六个系数、最终 $B_6=0$ 日志或任何新增谱因子。既有 18 条 (6) 的实际来源已经足够证明 (13)。

如果后续显式计算发现 $\chi_\lambda$ 含 $\lambda$ 或 $\lambda-3/2$ 的整式因子，只能依据：

- [原 U 值 atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)中 $\lambda=m/U_0\ne0$ 的原域定义；
- [整个 W 的 $\lambda=3/2$ 原支排除](R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)

来作相应局部化剥除，并对每次综合除法作完整系数乘回。未发现或未独立支付的其它谱根一律保留。这一可能的降次不作为本稿已完成结论。

## 6. 对已有两条 λ 六次原条件的无新逆降次接口

[十一原行与两条六次条件](R150-appendix-unit211-W-physical-lambda-eleven-original-rows-two-sextics-and-projection-boundary.md)已得两个标量原必要式 $C_i(\lambda)$，其对 $\lambda$ 次数为 6。旧源码在剥去已付的 $\lambda$、$3-2\lambda$ 因子时，对完整原迹同除该乘积，故其准确理想身份位于已付物理局部化
$
I_6^{\rm phys}
=I_6\,A_W[x,y,t,\lambda^{-1},(3-2\lambda)^{-1}],
$
其中 $\lambda$ 始终是 (8) 的同一仿射式。不能仅凭 $C_i$ 是多项式就退回未局部化的 $I_6$。本稿的 $\chi_\lambda(\lambda)\in I_4$ 则仍完全不使用这些值逆。

记 $C_i$ 的真实六次系数为 $a_i(e,k)$。由 (3) 直接得到

$$
\widetilde C_i(\lambda)=C_i(\lambda)-a_i(e,k)\chi_\lambda(\lambda)
\in I_6^{\rm phys},\qquad \deg_\lambda\widetilde C_i\le5.
\tag{17}
$$

式 (17) 仅沿用上述两个已付值逆；不倒置 $a_i$，也不倒置前稿未付的内容 $h_0,h_1$，因此保留这些头和内容的整个零纤维。这是下一个可用的原低度输入；本稿不声称已经展开 (17) 或完成它们的结式。

## 7. 可再生定义与准确执行状态

新源建议规范路径：

notes/2026-11-28-unit211-W-global-physical-lambda-six-characteristic-original-input-8542.py

Git blob：4ab79a61a35f942edb15cfecff2562ccc82e065f。

SHA256：563ef7c9682a4b52f30bea024a391588c747fd97b0a2e8a6c1a4f14a49ec2d65。

字节数：10134。新首次预算为 180 秒、4 GiB；冻结时尚无实际运行结果。

唯一依赖为：

notes/2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py

完整 SHA256：10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1。

实际执行的定义前缀截至必要行列表建立之前，长度 15191 字节，SHA256：

d4696b07ea7eccb62b4e8c885fb50e95f17b6c0d105eb65fb2a3d11b2f965507。

该前缀的全部乘法身份此前已在全 W 原六行定理的真实 run 46068841943 / job 140740627266 中完成。其源提交为 8b8da559c05cb1fb48d98f6b53daaf8fe0d321a3；真实内层退出码为 0。

本稿保存源、参数定义和小记录，不保存可重算矩阵、展开迹、特征多项式系数缓存或编码分片。
