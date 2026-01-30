# Risks, Mitigations & Deployment Notes

## Risk: JWKS Endpoint Unavailability
- **Risk**: Backend cannot verify JWT tokens if Better Auth JWKS endpoint is down
- **Mitigation**: Implement JWKS caching with fallback mechanisms
- **Detection**: 401 errors on all protected endpoints
- **Resolution**: Cache JWKS keys locally with periodic refresh

## Risk: Neon Free Tier Limits
- **Risk**: Database connection limits or storage limits
- **Mitigation**: Optimize queries, implement connection pooling
- **Monitoring**: Track database performance metrics
- **Contingency**: Prepare migration plan to paid tier

## Risk: CORS Issues
- **Risk**: Frontend cannot communicate with backend API
- **Mitigation**: Properly configure CORS middleware
- **Environment**: Different origins for dev/prod
- **Solution**: Dynamic CORS configuration based on environment

## Risk: JWT Verification Failures
- **Risk**: Signature algorithm mismatches or key format issues
- **Mitigation**: Properly validate JWT headers and payload
- **Monitoring**: Log verification failures for debugging
- **Resolution**: Ensure compatible algorithms between auth provider and verifier

## Deployment Notes
- **Frontend**: Deploy to Vercel with GitHub integration
- **Backend**: Self-hosted initially, consider Railway/Deta for PaaS
- **Database**: Neon Serverless with connection pooling
- **Auth**: Better Auth configured for production domain
- **DNS**: Custom domain mapping for professional appearance
- **SSL**: Enforce HTTPS for all production traffic
- **Monitoring**: Set up error tracking and performance monitoring