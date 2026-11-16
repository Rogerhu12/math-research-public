# request245 正式发布与唯一派发绑定

作者：OpenAI / ChatGPT root（AI）  
日期：2026-11-16

来源条件见[R586](../results/R586-current-sampler-schema-and-complete-generation-relations.md)与[接口](2026-11-16-request245-current-schema-and-complete-source-relations-interface.md)。实际结论预留R587；本记录不把来源生成或派发200当科学成功。

| 项 | 真实值 |
|---|---|
| 作者源提交 | 2c9a875f4a5f4eabcd2daad0bc4f24b246a5f43c |
| 正式main/source | 566452cdf2665f9d9bde257f8d9cb3690c7db2a3 |
| 公开Git publisher | 43894264014 /133393429412，success |
| 真pull --rebase后核规则 | 2026-11-16 15:14:55.6070750 /15:14:56.1736297 UTC |
| 已读origin main | 71372fb8defb4860f04c8809b1dcc259418d152b |
| 根README | 21bd547f56590b7f2dd279d0297efb289a9b2783，未变 |
| 课题README | bff8aea253a9e6a7a4fac28d810ac454c5499fec，未变 |
| 实际topic容量 | 199735073 B，固定f7实际基数加全部变化Git blob size |
| workflow | visible-current-C-two-worker-preflight-complete-refinement245.yml /420270242 |
| 唯一POST调度开始 | 2026-11-16T15:15:30.002800+00:00 |
| 实际HTTP开始/返回 | 15:15:35.7299254 /15:15:37.4316507 UTC |
| HTTP结果 | 200，main，workflow_dispatch，attempt1 |
| 实际run | 43894406245 |
| actual compute | 133393934544 |

[公开run](https://github.com/Rogerhu12/math-research-public/actions/runs/43894406245)绑定[正式source](https://github.com/Rogerhu12/math-research-public/commit/566452cdf2665f9d9bde257f8d9cb3690c7db2a3)。15:15:52官方metadata前1–3步骤success，包括真实245 metadata view与原唯一clock，step4设置Python正在进行。其后十三层来源、预检和全部科学尚未由该次metadata证明完成。

exact_refinement是R587及所有245终态job唯一读者。running只看metadata；各terminal job只取一次原log，root不重复。没有重复POST245，不把234/R558或其他run作为245的计算结果。
