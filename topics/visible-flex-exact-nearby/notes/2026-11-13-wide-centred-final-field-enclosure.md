# 宽领圈最终系数的中心混合 Taylor 包围

本说明给出一个区间求值改进及其可重放源码，不报告尚未运行的新数值。新源是 scripts/fourfold_phase_collar_centered_height_budget.py；其导入的原源 fourfold_phase_collar_correlated_height.py 固定为 SHA256 3752ac63322bc4008a898e7309f6ac46e2647290d86f3c330467950fa5b2cb42，不作修改。

原源的首个连续宽盒确已完成，执行证据和局部已读端点见 2026-11-13-wide-correlated-native-receipt.json。该次完整 JSON 在执行环境失联前没有保存，必须重跑。其后点值作业返回 exit 137，退出原因未知；本说明没有把它称为数学失败或已定位的内存故障。

## 1. 改进对象与保持的对象

仍使用同一准确 affine 参数族、真实无限 Fourier 原函数、同一根函数、六阶有限根坐标和四阶根匹配高度。几何身份及原始 Fourier 尾不变。新源只改变计算最终实函数值的次序：

1. 在盒中心计算最终组合后的系数 jets；
2. 用这些 jets 评价有限 Taylor 多项式；
3. 用整个盒上的真实高阶混合 jets 支付余项。

特别是没有先将两个接近抵消的最终量分别粗包围后再作差。区间运算中的实际参数依赖仍由原模型传入；以下 Taylor 论证逐个固定参数成立，因此允许各个中间区间丢失部分相关性，不能因此把包围变窄到真实值以外。

以中心 $r_0,\theta_0$ 和半宽 $d_r,d_\theta$ 表示物理实盒。原生 jet 的时间变量满足

$$
r=r_0-\rho w,\qquad \rho=2^{-10}.
$$

因此物理径向 Taylor 系数必须乘 $(-\rho)^{-i}$。这里 $\theta$ 始终是物理角，不是归一 Fourier 标签 $x=4\theta$。

## 2. 两个有余项的实 Taylor 展开

设 $f$ 在该盒及所用标量 spline germ 上具有所需有限阶连续混合导数。固定参数后，先对每一个 $r$ 在 $\theta_0$ 展开到 $n-1$ 阶，再对每一个保留的角系数在 $r_0$ 展开到 $m-1$ 阶：

$$
f(r,\theta)=
\sum_{0\le i<m,\;0\le j<n}
\frac{\partial_r^i\partial_\theta^j f(r_0,\theta_0)}
     {i!j!}
(r-r_0)^i(\theta-\theta_0)^j+\mathcal R.
$$

有

$$
|\mathcal R|\le
M_{0,n}d_\theta^n+
\sum_{j=0}^{n-1}M_{m,j}d_r^m d_\theta^j,
$$

其中

$$
M_{i,j}\ge
\sup_{\text{完整同一盒}}
\frac{|\partial_r^i\partial_\theta^j f|}{i!j!}.
$$

证明只用一元 Taylor 积分余项两次。第一项是固定 $r$ 的角向余项；其余各项分别是角向保留系数的径向余项。因此不需要额外假设混合复域解析性，也没有将未知混合系数填零。

若所需对象为 $\partial_r^a\partial_\theta^b f$，原 jet 中 $(i+a,j+b)$ 项的正确归一系数为

$$
\frac{(i+a)!}{i!}\frac{(j+b)!}{j!}
(-\rho)^{-(i+a)}
[f]_{i+a,j+b}.
$$

源码 scalar_coefficient 逐项实现这个公式；rectangular_enclosure 保留两个余项，不把混合的径向余项遗漏为单独的最高径向系数。

有限多项式通过实区间 Horner 评价。区间变量可跨零，乘法采用双线性乘法；未对跨零 Arb 区间使用可能产生 nan 的一般实幂。余项使用的幂底数均为非负的已知半宽或正的原生尺度。

## 3. 原生与无限尾仍在全部系数中

原 evaluator 的相关原函数过程是：

- 在准确 common scalar span 的准确中心形成完整有限 Fourier 原函数的径向 Taylor 系数；
- 在评价径向盒之前保留每个 Fourier 模的该多项式；
- 另外支付同一实际复圆盘上的径向 Taylor 尾；
- 保留原来的无限 Fourier / alias 尾；
- 用这些完整误差重新支付真实 $E$ 和曲率系数的误差。

新源直接导入该过程。它既不把节点误差当全角误差，也不从截断原函数免费推导无限原函数的高阶导数。

径向盒与中心两次求值必须处于同一准确 scalar span，且共享同一 native anchor。ordinary_fields 显式保留首次选定 span，并在改变中心前清除继承的状态缓存。不会跨越紧邻的 binary knots 误选 germ。全域覆盖尚需将每个真实 span 的适当盒实际计算，不能从一个盒推广。

在 root 原函数模型产生所需小 jets 后，新源仅保留坐标系数、根势系数和根高度有限 jets，再释放大模型。这是资源管理措施；没有据此断言先前 exit 137 的原因。

## 4. 新高度的完整主矩阵

真实坐标后的 grounded 主矩阵记为 $A$。新正高度 $\tau_*$ 是原真实归一高度的四阶根 Taylor 多项式。完整算子为

$$
P_*=-\operatorname{div}(C_*\nabla)+V_*,
\qquad C_*=\tau_*^2 A,
$$

$$
V_*=-\frac{\tau_*}{J}
 \operatorname{div}_{r,\theta}(B\nabla_{r,\theta}\tau_*).
$$

其准确拉回恒等式保持为

$$
P_{\rm ground}(\tau_*\,U\circ\Psi)
  =\frac{J}{\tau_*}(P_*U)\circ\Psi.
$$

三个误差项全部保留：

$$
E_{11}=(C_*)_{11}-1,\qquad
E_{12}=(C_*)_{12},\qquad
E_{22}=(C_*)_{22}-y.
$$

新源另外形成真正的相对矩阵项

$$
E_{12}/\sqrt y,\qquad E_{22}/y
$$

再对这些最终函数作上述中心包围。由于当前是严格正侧 ordinary 盒，源码先检查 $y>0$；不能把这里的除法用于尚未消根的 $y=0$ 盒。

若实际完整盒计算给出

$$
\epsilon=
\max\{\|E_{11}\|_\infty,\|E_{22}/y\|_\infty\}
+\|E_{12}/\sqrt y\|_\infty<1,
$$

则对同一真实盒

$$
(1-\epsilon)\operatorname{diag}(1,y)
\le C_*\le
(1+\epsilon)\operatorname{diag}(1,y),
$$

$$
A^{-1}\le
\frac{\|\tau_*\|_\infty^2}{1-\epsilon}
\operatorname{diag}(1,y^{-1}).
$$

该结论由实对称二阶矩阵的行和范数界直接得到。源码只有在实际 $\epsilon<1$ 时输出逆矩阵比较常数；它不从 $\tau_*^2$ 单独推断该常数，也不把短领圈原有的 $2.257$ 转授给新高度或宽领圈。

## 5. 实际 canonical 导数与 trial 范围

设真实坐标为 $(y,\phi)=\Psi(r,\theta)$。新源使用

$$
\partial_y=\frac{\phi_\theta\partial_r-\phi_r\partial_\theta}{J},
\qquad
\partial_\phi=\frac{-y_\theta\partial_r+y_r\partial_\theta}{J}.
$$

由此直接构造

$$
g_y=\partial_y\log\tau_*,
\qquad
g_\phi=\partial_\phi\log\tau_*,
\qquad
G\ge\sqrt{|g_y|^2+y|g_\phi|^2}.
$$

这些 canonical 导数与报告中的固定物理 $r$ 的角导数分列。没有用后者代替前者。

可选的 DB_without_Cphi、DC、LB 等仍来自此前已定义的真实物理多项式 $B,C$ trial。它们不是 R109 的准确 frozen-linear Airy trial。尤其不能把在物理角 $\theta$ 评价的 $v_0(\theta)$、$v_1(\theta)$，未经真实角标迁移就冒充 $v_0(\phi)$、$v_1(\phi)$。本源不作这种转授。

主矩阵的 $E_{11}U_y$ 弱通量项保持在完整误差中；普通源、所有低输出、均值、regular $\xi/\lambda$ 及外端 Wronskian 仍需在同一完整 gap 中接线。

## 6. 执行范围与重放命令

新源写成时执行环境不可用。没有新实际 JSON，不把源码中运行成功后才设置的 proved_specified_local_box 字段视为已完成门。

恢复后先在源码所在 topic 目录运行首个小盒，并立即保存整个报告，而不只保存摘要或 SHA：

~~~sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 MALLOC_ARENA_MAX=2 \
/home/agent/visible-exact-py0038/bin/python -u \
scripts/fourfold_phase_collar_centered_height_budget.py \
--radius 2423/10000 --radius-half-width 1/65536 \
--angle 1/16 --angle-half-width 1/2048 \
--nodes 512 --native-order 48 --bits 256 \
--without-trial-coefficients --emit-report \
--out notes/2026-11-13-wide-centred-height-first-box.json
~~~

解释器路径按实际恢复环境校验后替换，其他准确输入不变。随后才启动完整 trial 系数或下一盒。若源的真实高阶余项仍粗，则保留失败值并减小实际盒宽、提高有意义的有限阶或增加径向多项式相关性，不能删除余项。

该文件不证明完整宽领圈、全帽 gap、外端 Wronskian、全部反馈逆或非线性精确族。它解决的是此前实际宽盒中的区间相关性求值接口。
