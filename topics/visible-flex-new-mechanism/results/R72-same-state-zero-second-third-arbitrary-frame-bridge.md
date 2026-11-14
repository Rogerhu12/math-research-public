# R72：同一标量端态下任意 frame 的准确零二阶、零第三桥

日期：2026-11-14。独立短结论；使用 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) 的真实任意矩目标桥和 [R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md) 的真实倒行/第三 composition。父级与本代理已独立核对框架公式、半角及全部端态。没有新的几何、profile 或优化计算。

## 命题与范围

固定一个常值标量状态 $S=(k_*,h_*,\omega_*)$，其中 $h_*>0$。对任意目标 $R\in SO(3)$，存在有限长度的真实 $C^\infty$ 桥，从 frame I、状态 S 到 frame R、同一状态 S，两端都有常值 germ，满足

$$F_s=F\Omega(k),\qquad h>0,\qquad \omega_s=k_s/(2h),$$

且其二阶矩阵和完整第三算子准确为

$$M=0,\qquad \mathcal T(f;g,h)=0$$

对同一右 collar 为零的全部 profiles 成立。这里不指定中心曲线终点位移，也不声称第四常数项为零。

对构造使用的有限条桥，选择一个共同紧物理区间 I，使 $\xi+\omega\geq\delta>0$，之后固定该 I。此选择可在有限桥构造后完成；不把命题扩大成任意预先给定的窄区间必然可行。

## 1. 准确倒行与同态端口

令 $D=\operatorname{diag}(-1,1,-1)$。先用 R70 构造任意一条真实桥 B，满足标量首末均为 S、$F(0)=I,F(L)=A$、M=0，中心线末位移为 V。其归一化同 k 倒行是

$$F^R(s)=D A^T F(L-s)D,$$

$$\alpha^R(s)=D A^T\{\alpha(L-s)-V\},$$

$$k^R(s)=k(L-s),\quad h^R(s)=h(L-s),\quad
\omega^R(s)=\omega(L-s). \tag{1}$$

恒等式 $D\Omega(k)D=-\Omega(k)$ 保证 (1) 满足真实 frame 方程。它的首 frame 为 I，末 frame 为 $D A^T D$，标量两端仍为 S；任意常值 $k_*$ 都允许，不需要把 k 翻号或要求 $k_*=0$。

空间左旋转不改矩阵积分和 scalar range。因此 B 接上按其末 frame 旋转后的 $B^R$ 时，全部端 frame 和常值 germs 准确相接，整体 frame 增量为

$$A D A^T D. \tag{2}$$

倒行的 M 与原 M 相同，仍为零。由于 M=0 且保持真实右/s首锚，第二恢复倒行是偶的、Y 是奇的，所以

$$\mathcal T_{B^R}=-\mathcal T_B.$$

R71 的 composition 交叉项为 $-\Phi_{B^R}(f,\Phi_B(g,h))=0$。故真实复合桥满足 M=0、$\mathcal T=0$，没有用 formal 负号替代端口匹配。

## 2. 半角实现两个轴的任意旋转

取 $A=R_x(\theta/2)$。D 是 y 轴半周旋转，故

$$D A^T D=A.$$

于是 (2) 等于 $R_x(\theta)$。同理取 $A=R_z(\theta/2)$，得到 $R_z(\theta)$。对任意正负或模 $2\pi$ 的角，A 只是 R70 允许的一个具体 SO(3) 端目标；真实桥仍由有限正长度路径实现。

任意 $R\in SO(3)$ 都可选一个有限的 x-z-x Euler 分解

$$R=R_x(\alpha)R_z(\beta)R_x(\gamma).$$

分别构造上述三个零 M、零第三复合桥，再按实际 frame 顺序拼接，得到命题中的 R。只需有限六条 R70 原桥/倒行段，辅助整圈各自取有限值；没有无限拼接或极限曲线。这里不要求一套 Euler 角在整个 SO(3) 上光滑单值。

每段 M=0，故第三 composition 的交叉项全部为零，三段 T=0 的和仍严格为零。标量端态始终是同一个 S，所有常值端 germs 也相同。

## 3. 用途及没有支付的量

这使同标量端态的 frame 调整可以从 P1 的基准第三成本中完全分离：插入这样的 frame 桥不改 M 或 T，端 frame 则可准确达到任意目标。

它不解决不同 k/h/omega 标量端态之间的第三成本；这些真实转接的 T 仍必须按 R71 支付。它也不控制中心线位移。若它被插入 R45 的单 P，必须使用同一个修改后 P 的真实位移进行四块组装；对应的既有对称结构可支付全局位移闭合，不能把单桥位移另设为零。

即便 M=T=0，第四的 P0 和其他高阶局部成本也可能非零。命题没有支付 P0、完整第四 ruling、有限等距族、嵌入、reach 或宏观运动。
