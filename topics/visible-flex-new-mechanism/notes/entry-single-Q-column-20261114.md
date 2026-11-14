# 入口 $v_8$ 的一个准确角向自由列

日期：2026-11-14。状态：**已证明的表示与微分恒等式；实现待公开人工检查，不是候选计算结果。**

本稿只增加一个准确角函数乘一个现有径向基函数。它不改变完整固定度量、核心、帽或不可变高度参考；不执行优化，不声称误差下降，也不声称支付完整入口 Cauchy 数据。代码为 `scripts/frame_entry_single_q.py`，命令行只有人工 `--check-only`。

## 1. 动机与精确角函数

令椭圆核心的长短半轴为 $A>B>0$，材料角为 $\theta$，椭圆参数角为 $\phi(\theta)$。保持原准确弧长定义

$$
q(\phi)^2=B^2+(A^2-B^2)\sin^2\phi,
\qquad \phi_\theta=\frac{a_0}{q},
\qquad k=\frac{a_0AB}{q^3}.
$$

这里 $k$ 是单位切向关于材料角的转速，不是空间曲率。空间曲率为 $k/a_0$。设 $\Delta=A^2-B^2$，则

$$
Q(\theta):=\frac{k_\theta}{k^3}
=-\frac{3\Delta}{a_0A^2B^2}\sin\phi\cos\phi\,q^3.
$$

这是准确的 $\pi$ 周期奇函数。所需的下一项入口数据具有

$$
v_8=-\frac{\sigma CD}{4a_0}Q,
\qquad a'(t_c+x)=-Cx^3+Dx^4+O(x^5),
$$

其中 $\sigma\in\{-1,1\}$ 是上下半带符号，$D$ 必须取自完整冻结度量，不能仅取参考 seed。这个等式只在已声明的一侧 Taylor 类内使用，不从 $C^2$ 接合自动推出。

### 准确归一化

设 $s_*\in(0,1)$ 为

$$
B^2+(4\Delta-2B^2)s_*-5\Delta s_*^2=0
$$

的唯一正根，并定义

$$
D_0=\sqrt{s_*(1-s_*)}(B^2+\Delta s_*)^{3/2},
\qquad S_Q=\frac{3\Delta D_0}{a_0A^2B^2}.
$$

函数 $s(1-s)(B^2+\Delta s)^3$ 的导数等于

$$
(B^2+\Delta s)^2
\big[B^2+(4\Delta-2B^2)s-5\Delta s^2\big].
$$

方括号在 $0$ 处正、在 $1$ 处负，两个根异号。因此 $s_*$ 是区间中的唯一极大点，$S_Q=\|Q\|_\infty$。代码用此代数定义归一化，不用采样最大值：

$$
\widehat Q=\frac{Q}{S_Q}
=-\frac{\sin\phi\cos\phi\,q^3}{D_0},
$$

$$
\widehat Q_\theta
=-\frac{a_0}{D_0}
\left[(\cos^2\phi-\sin^2\phi)q^2
+3\Delta\sin^2\phi\cos^2\phi\right].
$$

浮点评价 $s_*$ 时按二次公式的符号选择等价有理化表达式，避免近圆时的相消；准确物理定义仍是上述唯一根。圆核 $A=B$ 时 $Q=0$，新模块拒绝添加零列，应直接使用原模型。

## 2. 只增加一个径向列

使用原场的五次夹持 B 样条首个保留基 $B_3(t)$，以及已发布入口权重 $W_5(x)$，$x=t-t_c$。新增

$$
v_{\rm new}(t,\theta)
=v_{\rm old}(t,\theta)
+\lambda_Q W_5(x)B_3(t)\widehat Q(\theta).
$$

所有原 $u,v$ 列和其系数标签均保留。$\lambda_Q$ 插在 $v$ 块末尾，高度块整体后移一位；当前实际固定度量模型由 $162$ 维变成 $163$ 维。一般人工模型维数以原维数加一记录，不硬编码 $163$。

该径向基是**原切向场**的基，不借用高度基的数量或 $W_4$ 权重。物理身份保存其完整有理 knots、degree、原 spline index、零延拓和准确角方向。

因 $B_3=O(x^3)$、$W_5=(x/\ell)^5$ 在入口附近成立，新列为 $O(x^8)$，不改已经嵌入的 $v_7$、位置二 jet 或开放核心。$B_3$ 在其支撑外为零，故也不改开放帽端口。其奇偶性保留 $m=2$ 的精确角闭合对称：水平切向在 $\theta\mapsto\theta+\pi$ 下反号，垂直切向由 $\theta\mapsto-\theta$ 消均值。

若原均匀 knot 间距为 $\Delta_s$，则

$$
B_3(t_c+x)=\frac{5}{3\Delta_s^3}x^3+O(x^4),
$$

所以新列的 $x^8$ 系数为

$$
\lambda_Q\frac{5}{3\Delta_s^3\ell^5S_Q}Q.
$$

仅要由这一列产生上节的所需 $Q$ 项，可取

$$
\lambda_Q=-\frac{3\sigma CD\Delta_s^3\ell^5S_Q}{20a_0}.
$$

这不是当前任意状态的总 $v_8$ 公式：原 $v$ 首径向行相对固定锚的非零差也会产生 $x^8$ 项。准确支付总 $v_8$ 还须同时处理这些旧列的首阶贡献，并检查系数盒是否容纳所需值。本模块不应用上述系数，也不执行该盒筛。$\lambda_Q=0$ 则在数学上准确还原父模型的场，不只还原有限采样点。

## 3. 同一高度与同一度量

仍使用

$$
T=\frac{(-\sin(\theta+u),\cos(\theta+u),v)}{\sqrt{1+v^2}},
\qquad X=a\Pi T+z(t)e_z,
$$

$$
z(t)=z(0)+\int_0^t b_0(s)\,ds+\sum_j c_j I_j(t).
$$

$b_0$ 永久来自原父模型的不可变锚，不用当前 $\lambda_Q$ 重新计算。所有 $c_j$、高度基 $I_j$ 和冻结 $a(t)$ 的物理定义均不变。因此新切向列不能悄悄改变共同帽高，也不能使原单一高度积分变成逐圈独立平移。以后若优化 $c_j$，仍须使用真实线性帽高约束和共同原函数。

数值实现调用原父模型在固定四角查询上的完整 geometry，仅读取已经与查询无关的共同 center、height jets 和 metric；不用该四角查询的切向、位置或曲率。新 $T$ 和其完整位置二 jet 在请求的完整均匀角网格上重新评价。这项复用的合法性来自父模型中共同 center 与当前 $u,v$ 完全无关，而不是低角分辨率已足够评价几何。

## 4. 完整位置二 jet 与参数导数

对任一切向参数 $p$，共同高度不变，故

$$
\begin{aligned}
\partial_pX&=a\Pi(\partial_pT),\\
\partial_pX_t&=a'\Pi(\partial_pT)+a\Pi(\partial_pT_t),\\
\partial_pX_{tt}&=a''\Pi(\partial_pT)
+2a'\Pi(\partial_pT_t)+a\Pi(\partial_pT_{tt}).
\end{aligned}
$$

角向与混合导数分别为 $a\partial_pT_\theta$ 和 $a'\partial_pT+a\partial_pT_t$。高度参数仍使用 $I_j,C_j,C_j'$ 三列，其他角/混合导数为零。

新增代码从实际 `basis_jacobian(...,'ss')` 取得带权径向二阶列，再按解析链式计算 $T_{tt}$ 的参数导数，避免将原未加权 $B''$ 误用于新增列。直接 metric 目标保持原定义

$$
e=|X_t|^2-1,\qquad q=X_t\cdot T,\qquad
\frac{1}{2N}\sum(e^2+2q^2),
$$

以及原 ball/strip 平滑正部形状项。没有把辅助 frame 残差重新引入目标。

## 5. 身份与检查范围

新空间、状态布局及新增准确角函数进入物理身份。原完整固定 metric、核心/帽、不可变 $b_0$ 和高度基身份保留。新列系数按实际 binary64 的准确有理数冻结。数值 $s_*$、弧长反解、GH/Nb/原函数求积规则只属于 evaluation 记录；不同 evaluation 必须重建同一物理身份。

准备的人工检查只使用已有人工 carrier，分别覆盖 paired 和 bounded 父模型：

- 零新列时六个位置 jet 与原模型的浮点差；
- 非零小新列时全部位置二 jet 的解析方向 Jacobian；
- 直接 metric 加原形状目标的方向 Jacobian；
- $\widehat Q_\theta$ 独立差分、完整端口列的消失；
- 原 metric 与不可变高度参考不变。

检查入口：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_entry_single_q.py \
  --check-only --out "$RUNNER_TEMP/entry-single-Q-check.json"
```

截至本稿写入，仅完成静态语法和纸面链式检查，没有本地运行人工数值或实际候选。本模块不读取实际状态作研究评价，命令行没有优化路径；是否用于后续真实联合求解应在九高度可行 stage 的实际输出后单独选择。

## 6. 已取得的公开人工回执

run43630999193/source3fedb0fd6b40d409d0f0fbf3da6c94fe9ae7c78a成功。两人工父场的zero-Q六jet差全0；完整位置二jet方向Jac相对差最多9.98e−9，直接目标方向Jac约1.01e−8，Q角导独立差分1.79e−10，端口列全0、原g和高度参考身份不变。人工维数18来自人工carrier，不冒真实163维候选评价。本模块仍未执行实际优化。
