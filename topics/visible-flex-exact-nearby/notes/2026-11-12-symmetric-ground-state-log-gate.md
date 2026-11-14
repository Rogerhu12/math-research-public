# 同一显式对称核心的真实 ground-state 对数门

状态：已由两个冻结连续证书用有向算术合并得到，未新增 Newton 或
改变候选。对象仍是原 step02 的 snapshot `bd9b4d14...`，范围
$|x|\le.25$、所有实角。

令
$$
Q=F_z/x,\quad G=Q/|F|,\quad u_z=F_z/|F|=xG,
\quad\ell=\partial_\theta\log G.
$$
在 $x=0$ 使用由奇性保证的连续延拓。已付常数为

$$
.8013746710724318<G<1.693932849043242,
\quad |\ell|<1.807518464345088,
$$
$$
|\ell_x|<27.579691856627,
\qquad |\ell_\theta|<59.324318529492.
$$

因此 $(\partial_\theta-\ell)u_z=0$ 在整个核心（包括腰圈）**准确**
成立。这提供 R37/R46 的同一个保 $z$ 平移核选择；不引入任意核心
$\ell$ cutoff。它不声称该公式已在尚未构造的帽上取得所需估计。

## 推导与正则阶数

前一标量证书给 $Q\ge q_->0$、$|Q_\theta|\le q_\theta$、
$|Q_x|\le q_x$。连续支撑证书给 $|F|\ge F\cdot\nu\ge h_->0$。
由于 $|F_\theta|=a$，
$$
|\ell|\le q_\theta/q_-+a_+/h_-.
$$
$Q\le\sup F_{x,z}$ 来自 $Q=\int_0^1F_{x,z}(tx)dt$，故相同证书
也给出 $G$ 的两侧界。

写 $A_j\ge\|a^{(j)}\|$、$G_j\ge\|\partial_x^j\gamma\|$，
$m_{\max}=96$。因为 $\gamma$ 准确为奇函数，
$$
|Q_{\theta\theta}|\le A_0m_{\max}G_1,
$$
而对积分表示微分给
$$
|Q_{x\theta}|\le\frac12
[A_2G_0+2A_1G_1+A_0(G_2+G_0G_1^2)].
$$
程序分别得到上界 40.10738080522405 与 14.322854125795532。
对 $\log|F|$ 使用真实 $F_{x\theta}=a'T+aT_x$，可取
$$
\begin{aligned}
|\partial_{x\theta}\log|F||
&\le3M_XA_0/h_-^2+(A_1+A_0M_{T_x})/h_-,\\
|\partial_{\theta\theta}\log|F||
&\le3A_0^2/h_-^2+A_0M_{T_\theta}/h_-.
\end{aligned}
$$
与 $\log Q$ 的对应商法则合并，得到所列 $\ell_x,\ell_\theta$。
没有用普通角采样替代任一全角范数。

该对象 $F\in C_x^4\cap W_x^{5,\infty}$，每个固定有限角导数也是
如此。积分表示使 $Q\in C_x^3\cap W_x^{4,\infty}$；正下界使商与
对数的链式法则有效。因此 $\ell$ 至少同属
$C_x^3\cap W_x^{4,\infty}$，满足 R46 严格区要求的更低阶
$C_x^2\cap W_x^{3,\infty}$。这里没有把全局五次样条宣称为 $C^\infty$；
实际 target root 的局部共同 span 则另外真实解析。

## 重放

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_log_ground_state_gate.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --scalar-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_core_scalar_gate.json \
  --core-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_core_interval.json \
  --out /tmp/visible-ground-state-log-gate.json
```

永久输出是 `data/phase_ring_continuation/type_fixed_step02_log_ground_state_gate.json`。
报告核对两个证书的同一输入 hash、全核心和闭单元覆盖，并记录全部源 hash。
后续复角分母门、首相位积分、真实传递与帽仍各须支付；本实门不替代它们。
