# R134 续篇：完整清分母多项式残差与第一次真实能量验证

2026-11-13，visible-exact-astra-ac0d。

**已执行结论。** 对同一原始腰目标及wholeη，完整有限候选先清分母、
再作全径向/全角多项式乘法，最后付真正目标余项和除数，能保留原来
点值区间式丢失的大量抵消。前三个连续闭盒的全原PDE残差已原生完成，
其R134两条线性能量屏障和含mean Sobolev门全部通过，准确区间为
\[
0\le r\le8995627274410713/9223372036854775808.
\]
真实零阶误差小于0.000109335031。第一个盒的完整残差
\(\rho_0<3.118699\cdot10^{-5}\)、\(\rho_1<0.006059747\)，
原同盒相关二阶区间Taylor给的值为0.104190和25.592275。
这是原完整PDE的严格残差改善；没有以有限谱方程的小残差代替它。

该新能量门不是当前最宽的存在性证书；同一分支的[-.07,.07]嵌入
仍由R132另行证明。完整.05新残差计算已启动，其长区间门尚未认证。

## 1. 在完整有限代数中清分母

候选 \(\widehat B,\widehat C\) 仍为R130保存的75段径向七次、
完整512角采样所定义的准确有限Fourier函数。以下简写B、C。
其残差为
\[
R_B=B_r-\gamma\partial_\theta((K+B^2)/C)+2\beta B,
\quad
R_C=C_r-\gamma B_\theta-\beta((K+B^2)/C-C).
\]
准确多项式分子是
\[
\begin{aligned}
N_B=C^2R_B
 &=C^2B_r-\gamma[2BB_\theta C-(K+B^2)C_\theta]+2\beta BC^2,\\
N_C=CR_C
 &=CC_r-\gamma CB_\theta-\beta(K+B^2-C^2).
\end{aligned}
\tag{CP.1}
\]
先计算这些分子的全部有限系数，再对连续径向区间和角圆取界。
所有mean和全部候选模仍保留。

在每个已付目标闭盒 \([r_-,r_+]\) 内置
\(r=r_m+hu\)、\(h=(r_+-r_-)/2\)、\(-1\le u\le1\)。
源代码从原共享端点dense递归准确展开B、C的全部八个u系数。
不是从有限径向采样重新拟合七次式。径向导数用准确因子1/h。

若原角度数为d，本次乘积分别至多3d、2d。程序强制Fourier网格
\(N>6d\)，本次为N=2048；完整u多项式相乘至多23次。
每个径向系数的所有角Fourier系数都通过有向FFT包围。
这个FFT是在已证明无alias的完整有限多项式代数中求乘积，不是
把三次非线性残差投影回原512网。原目标的无限尾并不进入这个
有限截断，仍由下一节的真正系数界支付。

## 2. 完整目标的二次模型与精确余项

对每个 \(f=K,\gamma,\beta\)，从原primitive/全部无限尾及wholeη
准确计算中心的 \(f(r_m),f'(r_m)\)。完整闭盒上的 \(f''\) 直接
消费R130完整150盒高目标报告。所有盒均保留原实际公共germ。
取三个明确dyadic数c0,c1,c2，分别为以下完整区间的中点选择：
\[
f(r_m),\qquad h f'(r_m),\qquad h^2f''([r_-,r_+])/2.
\]
令 \(f_m(u)=c_0+c_1u+c_2u^2\)。真正全盒余项可取
\[
\epsilon_f=
\sup|f(r_m)-c_0|+
\sup|hf'(r_m)-c_1|+
\sup|h^2f''/2-c_2|.
\tag{CP.2}
\]
Taylor积分余项立即给 \(|f(r)-f_m(u)|\le\epsilon_f\)，对正负u
都成立。选定c2不是声称真实二阶导常数；其全部变化在最后一项中。
前两项也保留完整参数不确定性和dyadic选择误差。

三个模型系数本身作为准确dyadic数参与有限Fourier乘积。
共同的scalar不确定性留在(CP.2)，不先复制到每个FFT节点而制造
无关高模不确定性。读取旧native时使用完整保存的上下端点，
不使用简短显示用ball字符串放大或缩小输入范围。

## 3. 原始无限PDE分子的全部剩余费用

写 \(K_m,\gamma_m,\beta_m\) 为上述模型，
\[
T_m=2BB_\theta C-(K_m+B^2)C_\theta,
\quad H_m=K_m+B^2-C^2.
\]
若 \(N_{B,m},N_{C,m}\) 是将三个模型代入(CP.1)的有限分子，则
\[
\begin{aligned}
|N_B-N_{B,m}|&\le\epsilon_\gamma|T_m|
 +|\gamma|\epsilon_K|C_\theta|+2\epsilon_\beta|BC^2|,\\
|N_C-N_{C,m}|&\le\epsilon_\gamma|CB_\theta|
 +\epsilon_\beta|H_m|+|\beta|\epsilon_K.
\end{aligned}
\tag{CP.3}
\]
这里交叉项已含在真正 \(|\gamma|,|\beta|\) 内，不漏
\(\delta\gamma\delta K\) 或 \(\delta\beta\delta K\)。
因目标系数与θ无关，角导误差准确由
\[
\begin{aligned}
|(N_B-N_{B,m})_\theta|
 &\le\epsilon_\gamma|T_{m,\theta}|
  +|\gamma|\epsilon_K|C_{\theta\theta}|
  +2\epsilon_\beta|(BC^2)_\theta|,\\
|(N_C-N_{C,m})_\theta|
 &\le\epsilon_\gamma|(CB_\theta)_\theta|
  +\epsilon_\beta|2BB_\theta-2CC_\theta|
\end{aligned}
\tag{CP.4}
\]
支付。特别有准确取消
\[
T_{m,\theta}=2(B_\theta^2+BB_{\theta\theta})C
                 -(K_m+B^2)C_{\theta\theta}.
\tag{CP.5}
\]
源代码对每个完整闭角单元分别评估(CP.3)–(CP.5)，保留它们与C
小分母位置的关系。并非只用一份全角最大Ct和最小C把所有费用叠加。

有限分子的角导也在收取径向变化之前逐个Fourier系数形成。
舍入不确定性有已知有限支持，因此角导误差可用Bernstein因子
\((4d_*)^q\) 完整支付；真实径向变化则在已经求导的系数上另行
作u区间Horner。原实角圆被4096个闭角单元覆盖，单元内Taylor
及所有有限Fourier补项仍完整计入。

## 4. Riemann残差与新的直接加权字段

在已验证的完整 \(C<0\) 图上准确恢复
\[
R_B=N_B/C^2,\quad R_C=N_C/C,
\quad P=(B+k)/C,\quad Q=(B-k)/C.
\]
真正Riemann残差仍为
\[
R_P=(R_B-PR_C)/C,\qquad R_Q=(R_B-QR_C)/C.
\tag{CP.6}
\]
导数通过(CP.6)的完整商式计算，k及其径向依赖是同一原目标的
\(k=\sqrt{-K}\)。准确目标恒等式已在R126支付，不能另换一个
候选曲率来消掉残差。

令 \(d_c=P-Q=2k/C\)。程序直接包围
\[
S_1=|(2B/C)_\theta|,
\quad \widehat W_0=\max(|d_cP_\theta|,|d_cQ_\theta|),
\]
\[
\widehat W_1=\max\bigl(|d_c(P_{\theta\theta}-P_\theta C_\theta/C)|,
 |d_c(Q_{\theta\theta}-Q_\theta C_\theta/C)|\bigr).
\tag{CP.7}
\]
利用 \(R_P-R_Q=-d_cR_C/C\)，完整加权残差可直接写为
\[
S_U=d_c(R_{P,\theta}-R_CP_\theta/C),
\qquad S_V=d_c(R_{Q,\theta}-R_CQ_\theta/C).
\tag{CP.8}
\]
因此本次同时保存 \(\rho_0,\rho_1,\rho_W\)，不再从没有一阶残差的
C0-only报告猜测或漏收 \(\rho_W\)。清分母、二次余项、角导取消、
(CP.6)–(CP.8)及完整degree7展开均已由独立代理逐项审核。

## 5. 真正执行R134的两条线性门

独立消费者 `fourfold_codazzi_weighted_error_barrier.py` 核全部原输入、
生产者和依赖SHA、准确中心/η范围、完整径向相邻端点及实际germ，
然后以T=1/16执行R134(134.15)–(134.17)。每盒都保存两个严格
微分余量和包含mean的Sobolev-C0门。

首次3盒已经真实通过，结果
\[
\sup\max(|p-P|,|q-Q|)<0.000109335030823<1/16.
\]
通过管门及真实gap后，R131准确线性系统支付实际一阶有限性。
候选在片间共享全部角Fourier端值，故没有漏掉径向状态跳跃；
允许径向导数分片跳跃，其残差按各实际germ积分。

同一新残差还由独立R131最大值消费者实际复跑。它明确适配新报告的
字段，核全部原身份，并从旧真实腰native独立读取加权初始角导数，
没有把候选导数当作实际初值。在同一3盒上，该最大值门更紧：
\[
e_0<6.167210\cdot10^{-8},\qquad q-p>0.2435189643.
\]
两种误差估计各自闭合各自完整门。当前短段上最大值法更好；新能量法
只给另一个已执行的合法估计，并不因使用了能量就自动更紧。

消费者在失败时保存全部已通过前缀、首次失败输入/门和有限数值，
`continuation_certified=false`；不将请求区间或已完成producer的
范围写成未经验证的解区间。完整.05的后续报告另存。

## 6. 冻结文件和复现

- `scripts/fourfold_codazzi_cleared_polynomial_residual.py`；
- `scripts/fourfold_codazzi_weighted_error_barrier.py`；
- `scripts/fourfold_codazzi_cleared_C0_continuation.py`；
- `notes/2026-11-13-Codazzi-cleared-polynomial-first-three-native.json.gz`；
- `notes/2026-11-13-R134-cleared-first-three-barrier-native.json.gz`；
- `notes/2026-11-13-R131-cleared-first-three-C0-native.json.gz`。

两报告分别保存生产者、全部输入及依赖的SHA；新输出路径可复跑：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_cleared_polynomial_residual.py \
  --rows 3 --out /tmp/Codazzi-cleared-first-three.json.gz
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_weighted_error_barrier.py \
  --input /tmp/Codazzi-cleared-first-three.json.gz \
  --out /tmp/R134-cleared-first-three-barrier.json.gz
```

这些局部验证不完成跨根、真实正帽、无限尾的共同匹配，也不改变
最终必须在同一公共度量族中支付全部几何标准的要求。
