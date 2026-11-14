# 同一 163 维曲面：把实际漏掉的细角约束加入固定 70 短步

**性质：实现定义、解析 Jacobian 与人工检查；没有本地研究几何评价。**

## 1. 为什么现在只改约束行

公开 run `43653520539` 的已接纳状态由 e407 变为

`06a603ec4aa254d29cb44fdcf60190fba356d8a6834eb73748d0755243db8736`。

两网最大曲率从约 73.35984 降至 70.72278；目标 70 尚未达到。三个全步的两网曲率均已低于 70，却因 768 网上的 metric 违反被拒。原 384 池没有任何遗漏违反行，故只继续同一粗网 LP 看不到真正阻挡它的细角约束。完整事实见 `notes/curvature-fixed-target-first-actual-result-20261114.md`。

新状态在 768 网的 metric 峰位于 $t=0.135$、$\theta=369\pi/384$。奇数角索引 369 不在原 384 网。距固定门 $167/625$ 仅余约 $1.58\times10^{-6}$。

本次保留原 163 个物理参数和全部原粗网池行。末片增加 17 列的另一纸面方案不启用。完整固定度量仍为

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

不可变 $b_0$、高度均值 384 节点、共同原函数、原参数盒、帽高、正高度、球、内条带、镜像和正则门全保留。固定目标仍为 $\lambda_\star=70$，不是新增物理变量。

## 2. 独立细行池与原索引

两个新源为：

- `scripts/frame_curvature_mixed_grid_steps.py`：新细行池、细网选行 Jacobian、固定目标短步控制器；
- `scripts/frame_curvature_mixed_grid_steps_audit.py`：十三份输入回放、单次公开运行、完整报告与紧凑语义摘要。

旧脚本不修改。原粗池的 11 组索引继续为

$$
g(N_rN_c)+iN_c+j,\qquad N_c=384.
$$

新增细池单独编码

$$
g(N_rN_f)+iN_f+j,\qquad N_f=768,
$$

包含只需要一阶位置参数导数的七组物理行：两个 metric 行、正高度、球、条带两侧、镜像点对行。曲率 PSD 的二阶 Jacobian 仍由原粗池支付；细网曲率继续完整实际验收。

每条新增细行记录原径向索引、768 角索引、物理 $t,\theta$ 的准确 binary64 有理数、$\theta/\pi=2j/768$、奇偶性及偶角对应的粗网索引。不能把奇角约束替换成最近粗角。

初始细池包含前一完整报告保存的细网 metric 峰，以及每个径向行、每个 metric 分支中行值不大于 $10^{-3}$ 的最多两个最小值。$10^{-3}$ 只是选择应送入 LP 的近活跃行距离，**不是验收容差**。物理容差仍用原配置。

每次已经实际评价的细网 trial，都用原七组容差检查全部点。遗漏违反行全部加入细池；若会超过显式 4096 行容量则保存并退出，保留最后合格状态。新增行不会删除旧粗行或旧细行。行池属于数值求解选择，不属于物理状态。

## 3. 真实细网 Jacobian

记 $U=X_t$、单位角切向 $T$、$e=|U|^2-1$、$f=U\cdot T$，固定 $\bar\eta=167/625$。两个行函数为

$$
c_-=\bar\eta-e-\frac{f^2}{\bar\eta},\qquad
c_+=\bar\eta+e-\frac{f^2}{\bar\eta}.
$$

对当前任一物理参数 $p$，

$$
e_p=2U\cdot U_p,\qquad
f_p=T\cdot U_p+U\cdot T_p,
$$

$$
(c_\mp)_p=\mp e_p-\frac{2f}{\bar\eta}f_p.
$$

这里 $g$ 固定，所以没有漏掉可变半径的列。$X_p,U_p,T_p$ 全来自原物理表示的解析导数。

其余五行分别直接微分。镜像行使用 $W=U\times T$、$z=X_z$ 与

$$
m=z^2|W|^2-\tau^2W_z^2,\qquad \tau=61/1000.
$$

令 $D=z^2W-\tau^2W_z e_z$，则

$$
m_p=2z|W|^2z_p+2(T\times D)\cdot U_p+2(D\times U)\cdot T_p.
$$

仍独立检查原正高度、正则和直接镜像半径；平方行本身不认证嵌入或整面 reach。

## 4. 小径向批不改变周期原函数

只取细池所需径向行，每批最多六个拥有行，附加原 $t=0,L$。每批仍计算**完整均匀 768 角点**，然后提取所需行。不能把孤立的几个角送进周期 $\Pi$，也不能把优化角集合当作高度均值的新积分规则。

调用的是原

`geometry(..., jacobian=True, full_two_jet_jacobian=False)`。

它返回全部普通位置二 jets，但只构造本批 $X,X_t,X_\theta,T$ 的参数 Jacobian。每批普通二 jets、固定 metric、共同 center 和 b/b′/b″，都与同状态完整 768 值缓存比较。沿用原 $5\times10^{-12}$ 相对浮点回放尺度；这是评价一致性核对，不是连续误差界。

在 163 参数、八个查询径向行、768 角点时，四个返回 Jacobian 块共

$$
4\times8\times768\times3\times163\times8
=96\,141\,312\text{ 字节}.
$$

这小于原粗曲率批的约 189 MB 返回数组。只保所选细行的最终 Jacobian；不建立 $7\times160\times768\times163$ 的完整细约束矩阵。Python/NumPy 中间场及原缓存仍会占内存，因此报告必须保实际 peak RSS，不能只凭上述返回数组估算宣布内存上限。

## 5. 保可行的求步与接纳

原 LP 模型、盒、帽高硬行、曲率 slack 和步长范数惩罚全保留，额外接入细物理行的解析 Jacobian。物理行没有 elastic slack。

每个准备接纳的候选必须先后通过原 384 和 768 完整值门，并使两网最大实际曲率严格下降；达到 70 与一般下降分别记录。不把 LP 预测、原 PSD slack 或被拒绝的低曲率 trial 当成合格物理状态。

若细网新违反行尚未在池中，加入后立即回到**最后一个两网合格状态**重新线性化，不再沿着看不到这些行的旧方向浪费后续回溯。若违反行已经在池中，则按原回溯减少步长。始终不以失败 trial 作为下一线性化状态。

预算原样：最多 12 个 LP 模型、40 次共享粗/细完整值评价、120 秒活动优化时间，每个模型至多六个回溯。初始化与 loader 时间单列并计入总壁时；最终同状态两网审计另记两次值调用，无第二次求解。每个试探、接纳状态和线性提案均保存完整准确 binary64 系数。

## 6. 十三份来源与新起点

前十二份输入及所有原 source、状态、$g/b_0$、采样和池身份严格沿用 `frame_curvature_feasible_steps_audit.py` 的回放。第十三份为

`notes/actions-43653520539-1-curvature_feasible_steps/curvature-feasible-steps-audit.json.gz`，

decoded SHA256：

`cd3f580a3ac0ae864a068d8305120f3fbfe0f03917a355a638721f482cf4ba90`。

新增检查它的 run/source、全部前十二输入字节绑定、原 e407 初态、完整 final state、准确系数、两网验收、最后接纳记录及全部已学粗行。唯一实际起点是报告保存的 06a603；没有捏造先前未保存试探，也不重跑旧优化。

原目标 70 未达和全部失败 trial 继续留在来源说明中。新状态身份不含行池、细 Jacobian 批次或固定目标。

## 7. 开发检查与公开调用

人工检查只涉及新功能：七组细行方向导数、奇角原索引、细行分批与完整细圈、失败细行加入后回到合格点、目标未达如实保留，以及十三输入完整人工 IO。人工完整曲面例还核同一周期原函数、共同高度与新细 Jacobian。

旧人工 IO 为避免其基准门阻挡，使用极大的 $\bar\eta=100000$。直接差分两个接近 100000 的行值会损失有效数字，因此开发输出同时保留该原始差分误差，并对数学上同导数的 $\pm e-f^2/\bar\eta$ 在加入固定常数之前作稳定差分；实际评价函数、实际 $167/625$ 门和容差都没有改变。

公开人工入口：

```bash
python scripts/frame_curvature_mixed_grid_steps_audit.py --check-only \
  --out "$RUNNER_TEMP/curvature-mixed-grid-steps-development.json"
```

实际入口沿用已发布 fixed70 workflow 的十二组路径和 expected SHA 参数，只更换 driver 并增加：

```bash
  --fixed-target-audit notes/actions-43653520539-1-curvature_feasible_steps/curvature-feasible-steps-audit.json.gz \
  --expected-fixed-target-sha256 cd3f580a3ac0ae864a068d8305120f3fbfe0f03917a355a638721f482cf4ba90 \
  --out "$RUNNER_TEMP/curvature-mixed-grid-steps-audit.json"
```

实际调用必须经过原公开 Actions/repository/topic 路径门。回放失败也保存 small JSON。每次 checkpoint 同时保存完整报告与语义 summary；summary 不重复全部 canonical、完整系数或逐径向大表，完整数据继续保留供复现。

本次实现不声称新细行一定使目标 70 可行，更不等价于精确等距、连续曲率界或整面 reach。它支付的是已经观察到、当前粗线性模型明确漏掉的一组约束。
