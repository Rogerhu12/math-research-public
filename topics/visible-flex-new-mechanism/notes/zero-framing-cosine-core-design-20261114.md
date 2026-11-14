# 零 framing 的偶 cosine 星形平核：设计器、冻结身份与双侧接口

日期：2026-11-14。状态：准确几何与零 framing 条件已推导，新设计脚本已写成独立模块；`repo_sources` 已只读审核主要导数与数据接口。执行环境失联，因此尚未运行新 Python 开发检查，也没有新 cosine 候选的实际求解或连续证书。首次真实计算仍由本公开仓库 Actions 执行。

## 1. 保留水平幅度来源，改变法向 framing

固定已公开筛查的强星形水平曲线

\[
r(\phi)=1+a\cos3\phi+b\cos6\phi,\qquad
\gamma_W=r(\phi)e^{i\phi},
\quad a=.65,\ b=.12.
\]

这组径向函数在 \([-1,1]\) 的变量 \(c=\cos3\phi\) 下为 \(1-b+ac+2bc^2\)，严格正，因此水平曲线仍是正则径向 Jordan 曲线。精确的投影距离与直径预算继续取同一个公开 planar certificate；不能把旧 sine lift 的三维高度、曲率或 J 证书沿用给本模型。

新的高度为

\[
\boxed{z(\phi)=z_0+\sum_{j=1}^{6}H_j\cos(3j\phi).}
\tag{1}
\]

六个 \(H_j\) 都是独立设计变量，不使用旧 sine lift 的尖谷系数消元。整体高度 offset \(z_0\) 可参与设计，也可通过 `--fixed-offset` 固定。它只改变位置，不改变速度、曲率、挠率或 J；最终仍与全部 \(H_j\) 一起精确冻结。

## 2. 为什么这一类具有零 framing

设 \(\kappa>0\)，记 \(T,N_F,B_F\) 为中心曲线的 Frenet 架。水平黑板架采用

\[
N_{\rm bb}=(y',-x',0)/p,\qquad p=\sqrt{x'^2+y'^2}.
\]

设 \(v=|\gamma'|\)、\(W=|\gamma'\times\gamma''|\) 和 \(A=x'y''-y'x''\)。Frenet binormal 在黑板法向平面中的两个分量准确为

\[
\boxed{
B_F\cdot N_{\rm bb}=\frac{p z''-p'z'}W,\qquad
B_F\cdot(T\times N_{\rm bb})=-\frac{vA}{pW}.
}
\tag{2}
\]

对于 (1)，\(r,z,p,v,A,W\) 都是偶函数，\(p',z'\) 都是奇函数。因此 (2) 的两个分量都偶，且它们构成一个单位圆值映射 \(F(\phi)\)。有

\[
F(-\phi)=F(\phi).
\]

圆周反射的 degree 是 \(-1\)，故

\[
\deg F=\deg(F\circ[-\phi])=-\deg F,
\qquad \boxed{\deg F=0.}
\]

水平投影为 Jordan，所以黑板参考 framing 的 linking 为零；加上相对绕数零，中心曲线沿 \(B_F\) 的 framing 也为零。这个结论需要 \(W>0\)，不能跨过 Frenet 曲率为零的未定义点。

R9 准确 rectifying 核满足中央材料导数 \(X_s=B_F\)，所以它的核心 framing 正是这里的零 framing。其离开中央截面的精确公式在正 J 范围内连续延拓该 framing。零 framing 消除了已发现的平圆领 linking 障碍，**不保证存在所需嵌入连接，也不证明准确核心本身在全部宽度上嵌入**。

## 3. 准确平核与真实二 jet

令 \(\ell\) 为中心曲线弧长、\(a_0=\operatorname{length}(\gamma)/(2\pi)\)、\(q=\tau/\kappa\)。材料角由

\[
a_0\theta=\ell+s q(\ell)
\]

的周期反解定义，准确场是

\[
X(s,\theta)=\gamma(\ell)+s(B_F+qT)(\ell),\qquad
J=1+s q_\ell.
\]

当 \(J>0\) 时，

\[
g_X=ds^2+a_0^2d\theta^2,
\]

\[
X_s=B_F,\quad X_\theta=a_0T,\quad
X_{ss}=\frac{\tau^2}{\kappa J}N_F,\quad
X_{s\theta}=-\frac{a_0\tau}{J}N_F,\quad
X_{\theta\theta}=\frac{a_0^2\kappa}{J}N_F.
\tag{3}
\]

唯一可能非零的主曲率为

\[
\lambda(s,\ell)=\frac{\kappa+\tau^2/\kappa}{J}.
\]

在整个 \(|s|\le w=.02\) 的准确最坏界是

\[
\boxed{\lambda_{\max,\text{width}}(\ell)
=\frac{\lambda_0(\ell)}{1-w|q_\ell(\ell)|},
\qquad \lambda_0=\kappa+\tau^2/\kappa.}
\tag{4}
\]

因此不能把它当成 \(X=\gamma+sB_F\) 的直柱外推，不能误设 \(X_{ss}=0\)。

## 4. 尖端与谷底自动零挠率，但 J 仍要检查

在 \(\phi=0,\pi/3\)，

\[
r'=r'''=z'=z'''=0.
\]

第一、三空间导数平行，故 \(\tau=0\) 是准确对称恒等式，无需消去任何高度系数。

然而 \(q_\ell\) 通常不为零。令该点的

\[
R=r''-r,\quad U=r''''-6r''+r,\quad
Z=z'',\quad V=z''''.
\]

则

\[
\kappa=\frac{\sqrt{R^2+Z^2}}{r^2},\qquad
\boxed{q_\ell=\frac{ZU-RV}{(R^2+Z^2)^{3/2}}.}
\tag{5}
\]

所以尖端、谷底的全宽主曲率仍是 \(\kappa/(1-w|q_\ell|)\)。新输出逐点给出 (5) 与完整导数公式的数值交叉核对，并始终标明“自动 \(\tau=0\) 不意味着 \(q_\ell=0\)”。

## 5. 实际设计问题

独立脚本：`scripts/space_star_cosine_design.py`。默认未知量是六个 \(H_j\)、一个 offset 和一个 epigraph 上界 \(T\)，共 8 个。固定 offset 时为 7 个。

在全部 collocation 角同时施加

\[
T(1-w|q_\ell|)-\lambda_0\ge0,\quad
1-w|q_\ell|\ge J_{\min},\quad
\kappa\ge\kappa_{\min},
\]

并最小化 \(T\)。默认 \(J_{\min}=.3,\ \kappa_{\min}=.1\)。这些是设计约束，有限采样通过不等于连续验证。

高度包含 offset。对均匀节点间距 \(h\)，使用

\[
\max_\phi|z(\phi)|
\le \max_{\rm nodes}|z|
+\frac{h^2}{8}\sum_j(3j)^2|H_j|
\tag{6}
\]

作为设计中的全角插值余项公式；最终浮点舍入和完整区间证书由独立验证器处理。高度导数对 offset 仅在零阶非零，AD 中没有把 offset 混进曲率。

设公开平面证书给 \(d_{\rm fill}\) 和 \(D_{xy}\)。因为准确材料核有 \(|X_s|=1\)，其每点相对同一材料中央点的距离至多 \(w\)。故核心的投影 padding 至多 \(w\)，条件位移见证至少 \(d_{\rm fill}-w\)。若将来整个闭面共用同一投影和高度包络，允许的中央绝对高度为

\[
H_{\rm allowed}
=\frac12\sqrt{\left(\frac{d_{\rm fill}-w}{.3}\right)^2-(D_{xy}+2w)^2}-w.
\]

默认再预留绝对高度 \(.02\)，让设计只使用 \(H_{\rm allowed}-.02\)。输出保存原始预算、实际设计预算和冻结候选的真实采样/插值余量。该预留不能替代未来完整连接带的高度认证。

## 6. 冻结身份与独立连续验证接口

顶层 `frozen_physical_identity` 为：

~~~json
{
  "height_basis": "cosine",
  "a": "13/20",
  "b": "3/25",
  "half_width": "1/50",
  "height_coefficients": [
    {"numerator": "...", "denominator": "..."}
  ],
  "height_offset": {"numerator": "...", "denominator": "..."}
}
~~~

`height_coefficients` 实际包含全部六个条目。每个选中的实际 binary64 \(H_j,z_0\) 用 `Fraction.from_float` 原值精确冻结，没有经格式化十进制再拟合；\(a,b,w\) 使用 CLI 指定的准确有理数。规范身份 hash 是

~~~python
sha256(json.dumps(identity, sort_keys=True, separators=(',', ':')).encode())
~~~

独立 `space_star_cosine_verify.py` 只消费这一个明确身份，不重新选择试验、不改系数、不优化。设计报告保留 `planar_certificate_source.sha256` 锁住原平面证书。冻结后继续做区间节点加密才是同一个几何输入的验证；设计期间 \(a_0\) 随高度变化，不是固定度量 refinement。

每个运行只做一个初值 case。设计器在第一评价、之后每 10 评价或 60 秒写入独立 checkpoint；选择规则是：有采样可行点时取最小 epigraph，否则取最小采样约束违反。报告同时保留 raw final 的身份和 dense audit，不把选择过程隐藏成优化器原始成功结果。连续可行性始终另标为未证。

## 7. 失去旧半转后，正确的双侧连接

偶高度仍具有竖直镜面对称

\[
S=\operatorname{diag}(1,-1,1),\quad
\gamma(-\theta)=S\gamma(\theta),\
T(-\theta)=-ST(\theta),\
B_F(-\theta)=SB_F(\theta).
\]

\(\kappa\) 偶、\(\tau,q\) 奇，所以准确材料反解进一步给

\[
X(s,-\theta)=S X(s,\theta).
\]

这不改变 \(s\)，因此不能沿用旧 proper 半转把一个半带自动变成另一半。未来必须从准确核心的 \(+w\) 和 \(-w\) 两口分别连接。

若用两边都朝外的局部参数 \(t\ge0\)，负侧入口的真实 \(X_t,X_{t\theta}\) 取相反号，\(X_{tt}\) 保持原号。两个径向度量 \(a_+(t),a_-(t)\) 可以分别设计，并在中央准确常值 \(a_0\) 条带完整匹配。

每个半带仍可利用 \(S\) 对称降低自由度：\(x,z\) 用 cosine 角模，\(y\) 用 sine 角模。两个同轴平圆帽保持同一材料角即可让全局 \(\theta\) 平移仍为同一个完整 \(g\) 的等距作用。这里只是正确接口；几何核的 \(\kappa,J,\lambda\) 和实际包络先通过后，才安排双侧闭合场。

## 8. 首次 Actions 命令与审核状态

固定 planar report：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json
~~~

其 SHA256 为 `ba03fc43af2c86ee61b7ca1a9fa541f9287222ef8bd4dcb155c35332c9def405`。

先运行纯人工开发检查：

~~~bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_design.py \
  --check-only --out "$RUN_DIR/cosine-design-check.json"
~~~

随后一个独立 case：

~~~bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_design.py \
  --a .65 --b .12 --height-modes 6 --half-width .02 \
  --initial-lift .15 --angles 768 --dense-angles 6144 \
  --j-floor .3 --kappa-floor .1 --height-reserve .02 \
  --max-iterations 400 --checkpoint-every 10 --checkpoint-seconds 60 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$RUN_DIR/cosine-core-a65-b12-h15.json"
~~~

另一初值若需要，应单独 lane、单独输出，而不是与本例共用一个 40 分钟串行预算。独立连续验证由对应 verifier 接收这个输出；同 lane 读取运行临时目录也是明确冻结后验证，不应再优化。

`repo_sources` 的只读审核已覆盖：cosine 相位各阶导数、offset 只进入位置、8 列 AD、\(q_\ell\) 不变量、(5)、精确 binary64 身份，以及 normal-chord sample 字典接口。该审核没有运行 Python。开发检查预置了单个人工六模样本的 Jacobian、反射奇偶、对称点公式和身份 roundtrip；当前尚无实际通过结果，不能提前称为 tested。

## 9. 完成门没有省略

即使新的 cosine 核通过连续正曲率、正 J 和局部厚度预算，也仍需证明：准确核心嵌入、两侧连接和封帽、完整闭面嵌入与 reach、全像 Hausdorff 位移、握持集合及固定度量收敛。零 framing 是应先满足的拓扑门，不是本课题完成标准。
