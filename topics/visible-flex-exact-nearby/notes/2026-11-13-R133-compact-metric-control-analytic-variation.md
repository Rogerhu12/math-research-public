# R133 诊断补篇：保留真腰与真帽的紧支撑径向度量控制

2026-11-13，visible-exact-astra-ac0d / newton_source。

**状态：精确族与解析变分公式已经推导；下面的回传积分仅为浮点诊断。**
本篇没有改变既有 $g_0$ 证书，也没有宣称找到了分岔根或固定度量的
非线性 flex。它在原仿射参数 $\delta$ 对第四模返回近乎相切之后，
给出一个明确、局部且可保留既有两端接口的新度量方向。

## 1. 一次明确选择的候选度量族

保持原函数 $a(r)$，对每一对下面列出的有理端点 $l<u$，分别定义
一个独立的一参数族
$$
g_\nu=E_\nu(r)\,dr^2+a(r)^2d\theta^2,
\qquad E_\nu=E\exp(\nu h),
$$
$$
h(r)=\begin{cases}
4096t^6(1-t)^6,&t=(|r|-l)/(u-l)\in(0,1),\\
0,&\text{其余位置}.
\end{cases}                                                    \tag{C.1}
$$
该函数为偶函数、$0\le h\le1$，两端的零 jet 直到五阶，所以它是
全局 $C^5$ 紧支撑函数。尤其四种选择都准确满足
$$
g_\nu=g_0\quad\text{于}\quad |r|\le1/20\ \text{以及}\ |r|\ge9/50.
\tag{C.2}
$$
因此原腰曲线、腰初始框架和整个 $|r|\le.05$ 的已证实际解可保留；
R133 的完整正帽 $[.239,25/8]$、实际 natural graft 与 R74 原 regular
对象也准确不变。改变支撑带内的既有 $g_0$ 证书不能自动转授给
$\nu\ne0$。这里的 $\nu$ 是**新目标度量的选择参数**，不是已经
固定一个最终度量以后可随 flex 自由改变的参数。

## 2. 准确标量公式与第四模变分方程

令 $\gamma=\sqrt E/a$、$\beta=a'/a$、
$\ell=K/C_0^2$ 为 R133 的旋转参考系数。直接微分曲率公式得
$$
\gamma_\nu=\gamma e^{\nu h/2},\qquad\beta_\nu=\beta,
\qquad
K_\nu=e^{-\nu h}\left(K+\frac{\beta\nu h'}{2E}\right).
\tag{C.3}
$$
设 $D=\gamma^2-\beta^2>0$ 为该旋转图的正性条件，则
$$
\ell_\nu=
\frac{Ka^2\gamma^2+\beta\nu h'/2}
     {\gamma^2e^{\nu h}-\beta^2},
$$
$$
\dot\gamma=\frac12\gamma h,\qquad
\dot\ell=
\frac{-\ell\gamma^2h+\beta h'/2}{\gamma^2-\beta^2}.
\tag{C.4}
$$
点号是准确解析导数 $\partial_\nu|_{\nu=0}$，不是两个独立 ODE
结果相减。对 $\nu\ge0$，若原 $D>0$，则新旋转图分母仍为正。

以固定腰归一化 $b_4(0)=0,c_4(0)=1$ 积分 R133 的第四模线性系统。
其两个变分初值为零，并满足
$$
\begin{split}
\dot b_4'&=-2\beta\dot b_4+4\gamma\ell\dot c_4
                 +4(\dot\gamma\ell+\gamma\dot\ell)c_4,\\
\dot c_4'&=4\gamma\dot b_4-\beta(\ell+1)\dot c_4
                 +4\dot\gamma b_4-\beta\dot\ell c_4.
\end{split}                                                     \tag{C.5}
$$
正帽不变，故实际正帽 $q_4(.239)$ 与 $\nu$ 无关。返回函数及其
解析变分为
$$
F_4(\nu)=b_4(.239;\nu)+q_4(.239)c_4(.239;\nu),\qquad
\dot F_4=\dot b_4(.239)+q_4(.239)\dot c_4(.239).
\tag{C.6}
$$
当前计算中 $q_4$ 仍取已保存的**浮点**真旋转帽回传值；R133 新的
有向区间证书另行保留，不能用本篇的很多有效数字替代其误差界。

## 3. 实际计算结果

producer 同时积分中心列和四个解析变分列。使用原准确仿射对象，
512 个 primitive 节点、DOP853、相对容差 $2\times10^{-11}$、
绝对容差 $2\times10^{-13}$、最大径向步长 $1/4000$。
完整到达 $r=.239$，11,474 次 RHS，实际运行约 87.91 秒。
中心结果为
$$
F_4(0)=-1.936340757013877\times10^{-5},\qquad
q_4(.239)=1.056180708410158.
$$

| 支撑 $[l,u]$ | 解析变分的浮点 $\dot F_4$ | 线性预测 $-F_4(0)/\dot F_4$ |
|---|---:|---:|
| broad：$[1/20,9/50]$ | $0.020478002128117505$ | $0.0009455711279349692$ |
| early：$[1/20,1/10]$ | $0.004349355515189773$ | $0.004452017661585408$ |
| middle：$[9/100,7/50]$ | $0.008006993310355086$ | $0.002418311945521041$ |
| late：$[13/100,9/50]$ | $0.009958317633599032$ | $0.0019444456666864367$ |

broad 列的终端变分为
$\dot b_4=.014923176922107968$、
$\dot c_4=.0052593511335489885$。
其 521 个诊断径向点给 sampled $\max|\dot K|=1.7580098544845315$
和 sampled $\max|h'|=34.561780344$；这些采样极值没有被称作
连续全域上界。

相较于另存的原 $\delta$ 解析变分
$\partial_\delta F_4\approx1.1380867735991\times10^{-5}$，这个
明确的局部度量方向显示了明显更强的数值横截性。该比较只用于选择
值得认证的参数方向；不能把线性预测写成一个已证明存在的零点。

## 4. 可重跑输入与尚未闭合的门

运行入口：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
python scripts/fourfold_codazzi_compact_metric_return_probe.py \
  --out notes/2026-11-13-R133-compact-metric-return-controls-floating.json
```

脚本拒绝覆盖已有结果。全部源、实际对象、正帽输入、递归 Python
依赖和报告的 SHA 见同目录的 compact-control manifest。

需要另行闭合的数学门包括：参数盒内的有向返回及导数，有限幅度的
nonlinear Codazzi 解，$m\ge8$ 的完整可逆补空间，腰总转角/位置
闭合与 mean 方程，以及 R119 真 nonlinear regular 尾余量。
本篇没有将有限模近似边界或自由外端均值换成这些条件。
