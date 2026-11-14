# 空间 star 准确平核：实现、消挠率参数和 Actions

准确几何证明见 `results/R9-rectifying-flat-core.md`。独立模块 `scripts/space_star_flat_core.py` 已冻结，未改动平面 star 的稳定脚本。所有 lift/宽度扫描进入公开 Actions；本地仅作单例微分和接口检查。

## 1. 模块接口及证书分层

`SpaceStarFlatCore(a,b,lift,mix=0)` 使用

\[
\gamma(\varphi)=\bigl(r\cos\varphi,r\sin\varphi,
 h(\sin3\varphi+c\sin6\varphi)\bigr),\quad
r=1+a\cos3\varphi+b\cos6\varphi.
\]

`evaluate(s,theta)` 按 numpy 广播输入，返回 `x,xs,xu,xss,xsu,xuu,normal,phi,J,principal_curvature` 和隐式材料映射残差。`a0` 为弧长积分所得平均半径。准确公式采用准确弧长；数值 evaluator 使用分段 Gauss 积分与有括区间的 Newton 反解，明确不把浮点弧长说成准确积分证书。

连续筛选以每个完整极角小区间的四阶位置导数包络计算 $\kappa,\tau,q=\tau/\kappa,dq/d\ell$。只有全部区间证明 $\kappa>0$，并且 $1-w\sup|dq/d\ell|>0$，才标记准确核在该宽度上的浸入和闭角条件已核。若某格无法证明 $\kappa>0$，其余格的数值包络只属于已解格，报告显式置 `bounds_cover_whole_curve=false`，不会冒充全圈证书。

在上述条件通过后，$\lambda=(\kappa+\tau^2/\kappa)/J$ 给连续主曲率上界。它仍不是 reach 下界。三条径向截面的法线弦结果单列为样本，不能当作非自交或全局 reach 证明。

## 2. lift 混合系数的准确消挠率公式

这里 $c$ 是 lift 的 `mix`，不是半径函数参数。原 `c=0` 始终保留。新 CLI 还接受 `valley-zero` 与 `tip-zero` 两个**有理公式标签**，以区别于近似小数 `.220`、`.187`。

在极角谷 $\varphi=\pi/3$，记

\[
r_v=1-a+b,\quad C_v=10a-37b-1,\quad t_v=28a-109b-1,
\]

\[
z_1=h(-3+6c),\qquad z_3=h(27-216c).
\]

当 $C_v\ne0$ 时，准确中央曲率是

\[
\kappa_v=\frac{|C_v|}{r_v^2+z_1^2},\quad
\lambda_v=\frac{|C_v|+(r_vz_3-t_vz_1)^2/|C_v|^3}
 {r_v^2+z_1^2}.
\tag{1}
\]

这是将谷点的三个位置导数直接代入 Frenet 公式得到的有理表达式。令挠率分子 $r_vz_3-t_vz_1$ 为零，得到

\[
\boxed{c_{\rm valley}=\frac{9r_v+t_v}{72r_v+2t_v}.}
\tag{2}
\]

在尖点 $\varphi=0$，记 $r_t=1+a+b$、$t_t=-1-28a-109b$，同理

\[
\boxed{c_{\rm tip}=-\frac{9r_t+t_t}{72r_t+2t_t}.}
\tag{3}
\]

对 $(a,b)=(.60,.09)$，(2) 为 $.220059246720270842\ldots$，(3) 为 $.186578393018356906\ldots$。程序用 Decimal 定向有理运算保存包络，只有准确公式标签才标记相应点的挠率确为零。`.220` 和 `.187` 仍是单独的近似候选。

混合 lift 仍为奇函数，并保持三重转动和 R9 的完整半转对称。最大绝对高度也重新计算：令 $t=3\varphi$，驻点满足 $4c\cos^2t+\cos t-2c=0$。程序由此求 $H=\max|h(\sin t+c\sin2t)|$，在空间预算中使用 $2(H+w)$，不会误用 $2(h+w)$。

消掉谷/尖挠率不等于消掉整条曲线的瓶颈。廉价实现检查的 $(h,c)=(.2,.20)$ 虽使谷点 $\lambda$ 从 $16.7143$ 降到 $4.7051$，64 点粗样本的全圈最大值却约 $30.22$，峰值移到了别处。该样本不是连续最大值证书，更不是一个合格候选；它说明必须检查完整角域。

## 3. 保留的严格否决与开发核对

原输入 $(a,b,h,c)=(.60,.09,.2,0)$ 的谷点由 (1) 给

\[
\lambda_v=16.714313701199067399\ldots.
\]

仅用早期已证明 $D\ge2.9896138$ 就有 reach/$D\le.02001228<.03$；现在读取实际 4096 段 Actions 证书 $D\ge3.0045259551$ 后，上界收紧为 $.0199129449$。因此这个具体准确平核不能包含于满足本题 reach 比例的闭曲面。这是准确位置二 jet 和真实曲线直径给出的必要界，独立于 BVP 残差。

两个单例开发记录是 `notes/space-star-flat-smoke-20261114.json` 与 `notes/space-star-flat-mix-smoke-20261114.json`。隐式材料映射残差约 $2.7\times10^{-14}$；位置/完整二 jet 的差分相对误差不超过 $6.2\times10^{-9}$；半转二 jet 误差约 $4.2\times10^{-12}$ 以内；代数 $E,F,G$ 恒等式误差约 $2.2\times10^{-16}$。N=32 的连续帧区间太宽，尚未证明整圈 $\kappa>0$，记录明确为未认证。这些开发数值不代替 Actions 精查。

## 4. 与实际平面证书的衔接

`--planar-report` 读取 `notes/actions-43590239302-1-star_core/star-core-geometry-grid.json`，验证 schema 和 Actions 状态，按准确十进制参数唯一匹配并记录来源 SHA-256。空间核的投影 padding 用 R9 的 $w$ 上界，距离预算为 $d-w$，直径预算为

\[
\sqrt{(D_{xy}+2w)^2+[2(H+w)]^2}.
\]

完整闭面仍须让所有过渡和帽满足同一预算，并验证固定材料握持与全局 reach；当前模块只产生准确局部核的候选检查。

## 5. 可直接执行的 Actions 命令

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_flat_core.py \
  --a .60 --b .09 --lifts .10,.15,.20,.25,.30 \
  --lift-mixes 0,.187,.20,.220,valley-zero,tip-zero \
  --widths .005,.01,.02,.03 --nodes 4096 --samples 1024 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$VISIBLE_OUT/space-star-flat-a60-b09.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_flat_core.py \
  --a .65 --b .12 --lifts .10,.15,.20,.25,.30 \
  --lift-mixes 0,.187,.20,.220,valley-zero,tip-zero \
  --widths .005,.01,.02,.03 --nodes 4096 --samples 1024 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$VISIBLE_OUT/space-star-flat-a65-b12.json"
```

sparse-checkout 需要三个脚本 `space_star_flat_core.py`、`star_core_geometry.py`、`folded_reference_geometry.py`，以及 `topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core`。除 numpy 外无新 Python 依赖。单一候选遇到明确几何求值失败时保存失败原因并继续其余候选；不把失败行记为已认证。
