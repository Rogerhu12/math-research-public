# R632：真动能幅值图与负中心导数支的完整记忆链

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。
**已证明：在下面非退化域内，真实曲率幅值可准确消去一个原偶端方程；固定基础
曲率的负中心空间导数后，该图覆盖所选负初速支的全部四偶共同根。**
这是新的真实函数输入图，不是四偶共同根或完整 ruling 根。物理盒、其余三个
端积分、正势、所有常规范以及主课题完成条件均仍须支付。

## 1. 从真实非零形状进入动能端零集

沿用 [R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)
的同一原运动学及四偶矩公式。取 $h,\kappa\in C^2([0,1])$、$h>0$、
$\kappa(0)=0$、$L>0$，并定义

$$
U=\int_0^1(h_x/h)^2\,dx>0,\qquad
K_\kappa=\int_0^1\kappa^2\,dx>0,
$$
$$
\eta_\kappa(x)=\int_0^x\frac{\kappa_y}{2h}\,dy,
\qquad d_\kappa=h\eta_\kappa-\kappa.
$$

以一个全程常数缩放曲率：

$$
\boxed{\alpha(h,\kappa,L)
=\sqrt{\frac{1+U/L^2}{K_\kappa}}>0,\qquad k=\alpha\kappa.}
\tag{1}
$$

由积分线性性，真实 $\eta=\alpha\eta_\kappa$、$d=\alpha d_\kappa$。
从而

$$
\boxed{K=\int k^2=\alpha^2K_\kappa=1+U/L^2>1.}
\tag{2}
$$

R612 的原恒等式遂给

$$
\boxed{8A_{t_1}(L)+2A_{p_1}(L)
=L(K-1-U/L^2)=0.}
\tag{3}
$$

这说明一个 $K<1$ 的非零基础曲线可以用明确的新物理曲率输入进入该端零集，
而不是把它的独立 stored 历史尾值设成零。若固定 $h,\kappa,L$，正幅值必须满足
$\alpha^2K_\kappa=1+U/L^2$，所以 (1) 是唯一正支。
它没有任意拉长时间，也没有改变完整正势的系数。

四偶共同根现在仍准确等价于原三个真实条件

$$
P=0,\qquad B+C/L^2=0,\qquad S-W/L^2=0,
\tag{4}
$$

其中 $P,B,C,S,W$ 全部在同一条实际 $h,\alpha\kappa$ 及其真记忆上按 R612
定义。式 (3) 不能代替 (4)。若 $U=0$，R612 已排除四偶共同根；本图不借该退化
面扩张覆盖声明。

## 2. 消除幅值冗余及准确覆盖范围

固定一个常数 $c<0$，只允许基础形状满足

$$\kappa_x(0)=c.\tag{5}$$

这移除了 $\kappa\mapsto b\kappa,\alpha\mapsto\alpha/b$ 的正缩放冗余。
现在取任一原四偶共同根，假设其真实 $k_x(0)<0$。
由 R612 有 $U>0,K>1$，令

$$a=k_x(0)/c>0,\qquad \kappa=k/a.$$

则 $\kappa_x(0)=c$、$K_\kappa=K/a^2$，而共同根的动能身份给

$$
\alpha=\sqrt{\frac{1+U/L^2}{K/a^2}}=a.
$$

所以式 (1) 准确恢复原 $k$，真 $\eta,d$ 也完全相同。这证明所选非零负中心
导数支的全部原共同根都被覆盖，且逆向恢复没有改变物理长度或形状。
**不涵盖零中心导数或正中心导数支。** 正比例还保留
$k(0)=0,k_{xx}(0)=0,k_x(1)=0$；原 h 的端 germ 条件独立保留。

## 3. 全部参数导数必须跟随全局幅值

任一形状及长度方向满足

$$
\delta U=2\int\frac{h_x}{h}
\left(\frac{\delta h_x}{h}-\frac{h_x\delta h}{h^2}\right),
\qquad \delta K_\kappa=2\int\kappa\,\delta\kappa,
$$
$$
\boxed{\frac{\delta\alpha}{\alpha}
=\frac{\delta U-2U\delta L/L}{2(L^2+U)}
-\frac{\delta K_\kappa}{2K_\kappa}.}
\tag{6}
$$

证明为对 $\log\alpha=\tfrac12[\log(1+U/L^2)-\log K_\kappa]$ 求微分。
因此

$$
\delta k=\alpha\delta\kappa+\kappa\delta\alpha,\qquad
\delta\eta=\alpha\delta\eta_\kappa+\eta_\kappa\delta\alpha,
$$
$$
\delta\eta_\kappa(x)=\int_0^x
\left(\frac{\delta\kappa_y}{2h}
-\frac{\kappa_y\delta h}{2h^2}\right)dy.
\tag{7}
$$

对空间一、二阶导数，$\alpha$ 是全程常数，故同样有
$k_x=\alpha\kappa_x,k_{xx}=\alpha\kappa_{xx}$；但参数微分仍必须含
$\delta\alpha$。物理 $\gamma=h_x/L,\upsilon=k_x/L,a=h_{xx}/L^2,b=k_{xx}/L^2$
还须包含 $\delta L$。
全部真 A、六 rho、从属中心、完整正势及两条原 ruling 继续消费这些链。
不能在形成 Jacobian 时冻结新算出的 $\alpha$。

## 4. 作为同一实际 C² 插值空间的新入口

该图不指定三角函数族。可直接使用当前 O4 的 65 结点实际 quintic Hermite
曲线：h 的 65 个值、63 个内部空间一阶导数及独立中心二阶导数；基础
$\kappa$ 的 64 个非中心值、63 个内部空间一阶导数；再加 L，共 257 个形状
变量。固定 $h_x(0)=h_x(1)=0$、$\kappa(0)=0$、$\kappa_x(0)=c$、
$\kappa_x(1)=\kappa_{xx}(0)=0$。其余结点二阶导数沿原速度 spline 规则产生，
共同的端值、一阶和二阶数据给同一个 C² Hermite 表示。

真记忆按 [R609](R609-true-integral-histories-and-kinetic-input.md) 直接积分；
四奇 A 使用原右端锚，四偶 A 使用中心零锚，六 rho 使用原更新式。
因此没有可独立调节来掩盖实际末误差的 eta/A/rho 结点。
全程两常规范可以继续采用 [R614](R614-complete-two-ruling-global-gauge-projection.md)
的完整离根投影链，包含其非零 residual 伴随项。
这与已付 R609/R614/R616 的 17 模函数族不同，不重做该旧族的端恢复或拟合。

此段只描述新入口，不声称有限结点空间已有 (4) 的根或其 Jacobian 满秩。
若空间加密，必须保持已选物理曲线的读出与新优化空间的改变分别登记。

## 5. 物理盒、固定曲线精化和绝对门

缩放后仍须实际检查

$$
.8<h<3,\quad \alpha|\kappa|<2,\quad
\alpha|\eta_\kappa|<1,\quad
|h_x|/L<6,\quad \alpha|\kappa_x|/L<6,
$$

以及原 L 范围、当前使用的中心支条件。它们没有由 (1) 自动支付。
缩放前的 coarse 或 fine 资格不能转给缩放后的曲线；必要重建应输出全部实际
物理 attainer，并形成新真实残差/Jacobian 的首输入，不能只重跑一次诊断后停下。

同一求积器上 (1)(3) 是有限模型的代数一致性，不是连续积分误差界。
对固定物理曲线精化必须冻结已选 $h,\kappa,\alpha,L$ 及全程常规范，直接重新
读全部原端量；不得在细层重新计算幅值后把变过的曲线称为固定曲线验证。
原单位 ruling、原端量及后继的绝对完成门保持，不以归一化残差替代。

本结果仅给更合适的实际输入图和完整导数。完整 ruling、period/pose、闭曲面、
固定 g、全时间嵌入/reach 与宏观握持仍未解决。
