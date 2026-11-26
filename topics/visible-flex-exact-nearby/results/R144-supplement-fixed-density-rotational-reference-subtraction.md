# R144 补篇：固定密度重投影的旋转参考相减与完整源恢复

2026-11-26，visible-exact-astra-198c63d-20261126。

**已证明新的准确载体等价式；没有新增数值结论。** 本篇把 R144 的固定 $(u,j)$ 均值重投影写成零初值、无 mean 多项式导数的线性方程，给出原完整 signed residual、初值与全部跳跃的准确恢复。其用途是固定 $\eta_0,\nu_0$ 上尚未计算的同径向高阶积分，不重算已经完成的全参数旧 row 包围目标。

旋转参考本身及其微分恒等式已经由 [R133 scalar mean，Q.3](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md) 证明；固定密度的重投影已经由 [R144 MV.14–19](R144-supplement-exact-nonlinear-mean-elimination-and-retraction.md) 证明。这里不把这些旧结论登记成新的数学成功。新的内容是二者在固定 $j$ 而不是固定 $v-\langle v\rangle$ 时的完整相减、接口恢复及同物理角的输出消费者。

## RS1. 同一个原对象与已付的旋转参考

在原四重反射 moving 角 $\phi$、normalized angular mean 和真实 $dr$ 上，固定一个 metric 参数。设真实旋转参考为 $s<0$，原有限中心为

$$
 \bar v=s+\alpha V,\qquad
 \bar u=\alpha U_{\mathrm{ang}},\qquad
 \bar m=\langle\bar v\rangle=s+w<0,\qquad
 w=\alpha V_0,\qquad
 \bar j=\bar v/\bar m .
 \tag{RS.1}
$$

本篇的 $U,V$ 两个标量记为

$$
 U=\langle\bar u^2\rangle,\qquad
 V=\langle(\bar v-\bar m)^2\rangle,\qquad
 J=\langle\bar j^2\rangle=1+V/\bar m^2.
 \tag{RS.2}
$$

它们不是原 Fourier coefficient arrays 的名称。对实际完整32角模中心，直接由 Parseval 得

$$
 U=\frac{\alpha^2}{2}\sum_{k=1}^{32}U_k^2,\qquad
 V=\frac{\alpha^2}{2}\sum_{k=1}^{32}V_k^2.
 \tag{RS.3}
$$

这是同一个 $r$ 上的完整多项式乘积，没有角采样，也没有截掉中心的非零频率。未知全解不因此获得有限频率支撑。

复用原 Q.3：

$$
 N_s=\frac{a^2}{s^2}=1-\frac{a'^2}{E_\nu},
 \qquad N_s'=2\beta K a^2,\qquad
 \beta=a'/a,\qquad N_s(0)=1 .
 \tag{RS.4}
$$

最后一个初值来自同一个腰端 $a'(0)=0,s(0)=-a(0)$。在使用的闭区间内保留 $a>0,s<0$ 及完整原参考定义；真实根 $K=0$ 不引入除 $K$ 或除 $\sqrt{|K|}$。

## RS2. 零初值的新主载体

令 $m^\flat$ 为 MV 的固定 $\bar u,\bar j$ 重投影均值，并记

$$
 Y=\frac{a^2}{(m^\flat)^2},\qquad
 n=\frac{a^2}{\bar m^2},\qquad
 D=Y-n,\qquad
 W=Y-N_s .
 \tag{RS.5}
$$

MV 的准确均值方程给

$$
 Y'=2\beta UY+2\beta K a^2J,\qquad Y(0)=1.
 \tag{RS.6}
$$

减去已付 (RS.4)，得到

$$
 \boxed{
 W'=cW+b,\quad W(0)=0,\qquad
 c=2\beta U,\qquad
 b=2\beta a^2\left(\frac{U}{s^2}+\frac{KV}{\bar m^2}\right).
 }
 \tag{RS.7}
$$

证明仅需将 $J=1+V/\bar m^2$ 代入 (RS.6)。因此对任意完整给定的原中心，(RS.7) 与 MV 的固定密度重投影是同一问题；没有要求该中心已经满足原 mean 方程。

准确恢复原差为

$$
 \boxed{
 D=W+(N_s-n)
  =W+\frac{a^2w(2s+w)}{s^2\bar m^2}.
 }
 \tag{RS.8}
$$

(RS.8) 保留原保存的 $w$，并未将其改为零。特别在腰端，

$$
 D(0)=1-n(0)=\frac{a(0)^2w(0)(2s(0)+w(0))}
                    {s(0)^2\bar m(0)^2}.
 \tag{RS.9}
$$

新 $W(0)=0$ 是参考相减的准确初值；原重投影对旧中心的非零初值误差仍恰在 (RS.9)。

负曲率区中 (RS.7) 的两项可以相消。计算时应以同一个径向变量的完整 Taylor 多项式及有向余项处理它们；把每项独立取绝对值会丢掉这种相关性。这里只改变表示，不预先保证输出小、正性成立或某个充分门通过。

## RS3. 与原 signed residual 的完整相同

原近似中心真实残差是

$$
 R_0=\bar m'-\beta\bar m
       \left(1-U-K(\bar m^2+V)\right),\qquad
 \tau=-2a^2/\bar m^3>0.
 \tag{RS.10}
$$

MV 已给每个实际光滑片上的完整方程

$$
 D'=cD-\tau R_0.
 \tag{RS.11}
$$

由旧 Q.5 或直接微分，

$$
 (N_s-n)'=c(N_s-n)-b-\tau R_0.
 \tag{RS.12}
$$

将 (RS.7) 与 (RS.12) 相加正好给 (RS.11)。所以新主积分不计算 $w'$ 或 $\tau R_0$，但并没有删除它们的作用。它们已通过准确参考微分、完整原 $U,V,\bar m$ 和恢复式 (RS.8) 全部计入。

用

$$
 G(r,t)=\exp\left(\int_t^r c(\xi)\,d\xi\right)
 \tag{RS.13}
$$

表示同一个前向归一化传播。对一切真实 PPoly mean 接缝 $r_i$，原完整表达式仍为

$$
 D(r)=G(r,0)D(0)
       -\int_0^rG(r,t)\tau(t)R_0(t)\,dt
       -\sum_{0<r_i<r}G(r,r_i)[n]_i ,
 \tag{RS.14}
$$

端点处按一致单侧约定。令

$$
 A_D(r)=-\sum_{0<r_i<r}G(r,r_i)[n]_i,\qquad
 B_D(r)=D(r)-G(r,0)D(0)-A_D(r).
 \tag{RS.15}
$$

则 $B_D$ 准确等于 (RS.14) 中的完整 signed bulk integral。它可以从新主载体和完整接口和恢复；不是将 signed integral 的上界重新命名为实际积分。保存时须保留完整有向球，不能只保存 midpoint 或符号有利的一侧。

(RS.13) 是 $Y,D,W$ 的归一化传播。回到 MV 的 $h=m^{-2}$ 时，真实核仍为

$$
 \left(\frac{a(t)}{a(r)}\right)^2G(r,t).
 \tag{RS.16}
$$

旧 $a(r)^{-2}$ 放大没有消失。

## RS4. 全部接口及新场的真实跳跃

原真实 metric 的 $a,s$ 连续，故 $N_s$ 连续。原 PPoly 的 $U,V,w$ 可以有实际左右差。线性方程 (RS.7) 用完整的分片系数，以连续解 $W$ 跨过这些接口；$b$ 的跳不会在其积分中产生未登记的 Dirac 源。因此

$$
 [W]_i=[Y]_i=0,\qquad [D]_i=-[n]_i .
 \tag{RS.17}
$$

这与 (RS.14) 的每个 signed atom 完全相同。左右 $n$ 必须由真实左右原多项式及共同 $a,s$ 取得；不能把旧已完成对象的 tiny jump 换成准确零。若计算还分别记录 $A_D$，其递推是片内 $A_D'=cA_D$、接口 $A_D^+=A_D^--[n]_i$，每个原接缝恰计一次。

在 $Y>0$ 时恢复 $m^\flat=-a/\sqrt Y$；它连续。因此新完整场的跳为

$$
 [u^\flat]_i=[\bar u]_i,\qquad
 [v^\flat]_i=m^\flat(r_i)[\bar j]_i .
 \tag{RS.18}
$$

均值跳归零不等于全场连续。原全部非mean transmission、连续修补和最终 $C^2$ matching 仍须完整支付。对真正连续的 repaired 中心，(RS.18) 才依其已证连续性简化；本篇不将 raw ac1 偷换为 repaired selected family。

## RS5. 全域正性、同材料角与 physical 输出

必须在每个完整闭盒上证明 $Y>0$，而不只是各节点。满足该门后令

$$
 q=\sqrt{n/Y}>0,\qquad
 m^\flat=q\bar m,\qquad
 v^\flat=q\bar v,\qquad
 u^\flat=\bar u.
 \tag{RS.19}
$$

因为 $\bar j$ 不变，真实材料角

$$
 \Theta=\phi+I_\phi(\bar j-1)
$$

也完全不变。原密度正性仍来自原完整对象；$Y>0$ 本身并不新证 $\bar j>0$。

有理化的准确差是

$$
 q-1=-\frac{D}{\sqrt Y(\sqrt n+\sqrt Y)},\qquad
 \|v^\flat-\bar v\|_{A^0_\phi}
   =|q-1|\,\|\bar v\|_{A^0_\phi}.
 \tag{RS.20}
$$

例如 $Y\in[Y_-,Y_+]$、$n\in[n_-,n_+]$ 且两个 lower 严格正时，用正端点核

$$
 \frac1{\sqrt{Y_+}(\sqrt{n_+}+\sqrt{Y_+})}
 \ \le\
 \frac1{\sqrt Y(\sqrt n+\sqrt Y)}
 \ \le\
 \frac1{\sqrt{Y_-}(\sqrt{n_-}+\sqrt{Y_-})}
 \tag{RS.21}
$$

即可包围 (RS.20)。不能因一个过宽中心半径乘积球含零，就认为真实正分母可为零；也不能在 positivity 未付时使用此式。

同一个 $\Theta$ 下的原物理 $B,C$ 共同乘 $q^{-1}$。特别 full physical even mean 准确满足

$$
 \boxed{
 \langle C^\flat\rangle_\theta-\langle\bar C\rangle_\theta
 =\frac1{m^\flat}-\frac1{\bar m}
 =-\frac{D}{a(\sqrt Y+\sqrt n)} .
 }
 \tag{RS.22}
$$

这里使用完整角换元 $d\theta=\bar j\,d\phi$，不是 moving 非mean 投影。外 mean 只有在这个完整差确为零时才保持不变；否则它是实际新的 signed boundary source。外 $B$、非mean $C$、独立 height/farlabel、cap chart 输入和真实 boundary matching 仍须分别消费。

新非mean PDE 残差严格用 MV.19；新 $Y$ 或 $W$ 并不使那两条残差自动归零。

## RS6. 新科学输入与已完成目标的界限

旧全 $\eta$ row-range forward 目标已经在 [R144 actual](R144-supplement-actual-forward-mean-enclosure-and-unresolved-gates.md) 完整完成并锁定。它的三个 unknown 门不是数值反例，也不授权重跑同一已完成输入。

下一消费者固定原 $\eta_0,\nu_0$，在 (RS.7) 的同一个径向变量上建立新的高精度 Taylor 载体和完整余项；原完整32模/6144 PPoly pieces、全部6143接缝和真实 metric/graft 分段须绑定。原已经保存的 point 域只读；确实未保存的新载体可以作为新目标的必要私有输入物化，但不得声称旧目标原本已给它，也不得把旧 residual/Green 积分再登记为新成功。

输出须覆盖整个闭区间，保存完整 signed $W,Y,D,G,A_D,B_D$ 及需要的全域门或真实见证。任何有限前缀、局部正性或 tiny 腰误差都不推出全域 $C^0$、true selected $\delta_*$、真实 PDE/phase 解或最终闭等距族。所有细格数组留在公开 Actions runner 的临时私有工作目录，只发布脚本、参数、实际 run/哈希与小型完整结论。
