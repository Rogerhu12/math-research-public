# R749 — 实际非线性C²等距局部延拓及完整有理系数公开运行

会话 Astra-larger-e4e2a2bf-20261126。完整证明与三件可执行源原子刊出；实际run/job/系数检查返回均尚未观察，不把解析存在证明或源代码当真实运行。

## 已证明的精确范围

[完整R749证明](../results/R749-fractional-Darboux-exact-local-continuation-at-the-displaced-straight-wall.md)在真实R746/R747右圆弧材料、移到物理平直墙的入口二jet下，以z=v^(5/2)u将整个Darboux方程转为以纵向x为演化变量的解析非特征CK方程。正W²下bar g=g−dz²解析且平坦，完整平面展开给X,Y并逐条付全入口二jet，故真C²非C³解在一个正宽矩形严格同g，而非仅有限formal jets。一个同矩形适用于两端和θ∈[1,π/2]。

可将此真解用O(δ^1/2) C²小修改裁拼进原完整闭场，保全相位reach≥.106、D0<3.40、held>1.520、grip≥1.40与δE>0，θ∈[1.1,π/2]的更小真子带严格等距；裁拼区、剩下圆端与帽仍未付。宽度存在但本证明没有可用数值下界，也没有全域收敛或完成声明。

## 原完整公开运行

标准库Fraction计算，不调用本地科学。真实固定r_y=27/250、ε_y=1/2000、κ=20/3、z次幂5/2；两个独立h0=1和64。每支依次完整(x,v)次数(4,8)、(8,12)、(12,16)，逐元复算完整非线性Darboux余式；检查行0…xdegree−2/列0…vdegree，全部重叠有理系数逐字一致。有限系数和零余式不付解析半径。完整有理raw仅runner，完整summary/源身份/原参数/所有失败未知在main note。

```text
python -u topics/visible-flex-larger-amplitude/scripts/resume_20261126/r749_fractional_darboux_coefficients.py --orders 4 8 12 --radial 8 12 16 --heights 1 64 --raw "$RUNNER_TEMP/r749-exact-series.json" --summary "$RUNNER_TEMP/r749-actual-report.json"
```

公开workflow checkout main后真实pull/rebase并核两README，标准库默认Python，job上限30分钟；全6盒没有新增科学wallclock切断/早停。完整返回后发布器先metadata总量、正常pull/rebase、非快进即继续循环；全报告<100KB才提交。实际科学run/attempt/source/results直到官方和完整note返回才填写。GITHUB_TOKEN由Actions提供，不写用户凭据。

## 整件身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/results/R749-fractional-Darboux-exact-local-continuation-at-the-displaced-straight-wall.md",
    "bytes": 12953,
    "sha256": "f2664d80027548f0859bb15ae5cb7493d9a1e2ce96a1f9ef1c6fa563f1f566b5",
    "git_blob_sha": "9499932b2ae7d4399ed62b97491ffafbd5c501cc"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r749_fractional_darboux_coefficients.py",
    "bytes": 7441,
    "sha256": "d07afa956b4edb43c0da5e5458afa5e498f79d10f29a1f1d7e5b0e8ae81b61c6",
    "git_blob_sha": "a07404a8c70059fe34bad06637921bd904194c0d"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/publish_r749_darboux_coefficients.py",
    "bytes": 5970,
    "sha256": "4c51351531b9abd217440e6cf6c843c786c3365dc4616df7ec780f2dc56e228c",
    "git_blob_sha": "049508a588b087893633ddbb102e39756de26e15"
  },
  {
    "path": ".github/workflows/visible-larger-r749-fractional-darboux.yml",
    "bytes": 2693,
    "sha256": "8f3f35b32107b07dbcbca4d49c5dbe15d9a8e15e32507d982a9ae97816f912e7",
    "git_blob_sha": "00c51ce846ffc625c2a77f0f8c489567a9199369"
  }
]
```

所有source已完整读过，实际字段当前null；不能借同形式旧数值。

## 2026-11-28 13:13:32 UTC — R749 原6个有理盒全实际返回

官方run46148020052/1、job140988230946均completed/success，触发9a5e987a282c5ef7d4aafe5abb8532e4138ec2b8；真实source与双README真pull都为41e47abdc5a7634437a026ecccd54dfd31c400a6。原h0=1、64（两个值）的三原矩形全部返回：每支45/117/221个系数，原完整残差框3×9、7×13、11×17，六盒所有检查余项都为准确有理数零，四次可比嵌套逐项相同。两支u[x²,v⁰]为160000000000000/243与2500000000000/243。raw30074B/c6f8540fefe01a59e107380736172e8b7706be934ab28bac44bf569344d7c3cd仅runner，所有6盒各自完整身份如下原文。

这是实际有限代数验证；其证明意义只限指定框，不给解析半径或全端闭解。R749正文的真实非线性正宽由独立CK证明支付，R750更大高度的缩放与显式宽度是另一事实，不把本次h=1,64数值借过去。

```json
{"actual_target":{"d5":"1000000000000/27","eps_y":"1/2000","kappa":"20/3","material":"s0=s1+eps_x/2+r_x*(pi-.5), right straight-wall trace after s+r_x*theta","r_y":"27/250","z_power":"5/2"},"attempt":"1","boxes":[{"bytes":966,"checked_residual_columns":9,"checked_residual_rows":3,"coefficient_count":45,"first_nonzero_residuals":[],"key":"h1-x4-v8","nonzero_coefficients":19,"number_nonzero_residuals":0,"previous_box_identical":null,"sha256":"adf4d9c8bbc6db654c4a837bbc633bc7ee4ee0bb1e6adf111719ffd76968dabd","u_x2_v0":"160000000000000/243","u_xlast_vlast":"3428249600344649812262000000000000000000000000000000000/903981141"},{"bytes":4032,"checked_residual_columns":13,"checked_residual_rows":7,"coefficient_count":117,"first_nonzero_residuals":[],"key":"h1-x8-v12","nonzero_coefficients":53,"number_nonzero_residuals":0,"previous_box_identical":true,"sha256":"4f6207a0730d50772ddfded13eb1a18adf5a9e507dfa0a94dde2c451252ea636","u_x2_v0":"160000000000000/243","u_xlast_vlast":"1193756768822116817732421615141678372412502400478759765625000000000000000000000000000000000000000000000/12971141321962887"},{"bytes":10756,"checked_residual_columns":17,"checked_residual_rows":11,"coefficient_count":221,"first_nonzero_residuals":[],"key":"h1-x12-v16","nonzero_coefficients":103,"number_nonzero_residuals":0,"previous_box_identical":true,"sha256":"f8cd75f5682be6a701ac784a6a345755ce6053e7d8328e8b62118b0adddc8f96","u_x2_v0":"160000000000000/243","u_xlast_vlast":"8949197325040532716438243535269316200170681950154745251565931791562726617187500000000000000000000000000000000000000000000000000000000000000000000000000000/135818402393433899416854638061"},{"bytes":909,"checked_residual_columns":9,"checked_residual_rows":3,"coefficient_count":45,"first_nonzero_residuals":[],"key":"h64-x4-v8","nonzero_coefficients":19,"number_nonzero_residuals":0,"previous_box_identical":null,"sha256":"21969c1a62a463b33abeac48de9b639cdee9c14a0e42e0cea60d21b727a4cfe2","u_x2_v0":"2500000000000/243","u_xlast_vlast":"13077755744234768000000000000000000000000000000000/903981141"},{"bytes":3666,"checked_residual_columns":13,"checked_residual_rows":7,"coefficient_count":117,"first_nonzero_residuals":[],"key":"h64-x8-v12","nonzero_coefficients":53,"number_nonzero_residuals":0,"previous_box_identical":true,"sha256":"28c557af3b6d92da3855cd68ecc5a8e1b8e288cd9d6cc11cb5215bbdf5ea33e2","u_x2_v0":"2500000000000/243","u_xlast_vlast":"271428873969359530613528692544880640625000000000000000000000000000000000000000000000000000/12971141321962887"},{"bytes":9668,"checked_residual_columns":17,"checked_residual_rows":11,"coefficient_count":221,"first_nonzero_residuals":[],"key":"h64-x12-v16","nonzero_coefficients":103,"number_nonzero_residuals":0,"previous_box_identical":true,"sha256":"c341c8f720f48c91116649559c9beb317c4a0ecdd85b6b639914bb805ef0260d","u_x2_v0":"2500000000000/243","u_xlast_vlast":"121285209754847883534812013748758260886448706072651856323242187500000000000000000000000000000000000000000000000000000000000000000000000/135818402393433899416854638061"}],"rules_read_commit":"41e47abdc5a7634437a026ecccd54dfd31c400a6","run":"46148020052","schema":"R749-actual-rational-Darboux-CK-coefficients-v1","scope":"Exact truncated coefficient/residual identities. No analytic width, convergence-rate bound, global metric certificate, or mesh is inferred from finite coefficients.","source_commit":"41e47abdc5a7634437a026ecccd54dfd31c400a6","source_script":{"bytes":7441,"sha256":"d07afa956b4edb43c0da5e5458afa5e498f79d10f29a1f1d7e5b0e8ae81b61c6"},"trigger_commit":"9a5e987a282c5ef7d4aafe5abb8532e4138ec2b8","whole_raw":{"bytes":30074,"sha256":"c6f8540fefe01a59e107380736172e8b7706be934ab28bac44bf569344d7c3cd","uploaded":false}}

```


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/r749-actual-darboux-coefficients-46148020052-1.json",
    "bytes": 3704,
    "sha256": "bbb5f068841096653f5e8f7af3487f0b9c38125afa6c2c53bd125d3351c5e271",
    "git_blob_sha": "6a5e22b060c8c894cc7c60bbfd01ad80620d7a64",
    "fixed_commit": "5aca233301cd402b4dc613e2ef59c3b4d01ed8fa",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```
